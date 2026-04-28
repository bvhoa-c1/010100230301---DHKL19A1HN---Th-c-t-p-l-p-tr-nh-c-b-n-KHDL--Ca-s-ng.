
import os
from flask import Flask, render_template_string, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# ==========================================
# 1. CẤU HÌNH ỨNG DỤNG (APP CONFIGURATION)
# ==========================================
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hus-secret-key-2026'
# Sử dụng SQLite để dễ dàng chạy thử mà không cần cài đặt database server phức tạp
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hus_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Vui lòng đăng nhập để truy cập Cổng thông tin HUS."

# ==========================================
# 2. ĐỊNH NGHĨA CƠ SỞ DỮ LIỆU (MODELS)
# ==========================================

class Student(UserMixin, db.Model):
    """Bảng Sinh viên (Kế thừa UserMixin để tích hợp Flask-Login)"""
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_code = db.Column(db.String(20), unique=True, nullable=False) # Mã sinh viên (VD: 22001122)
    full_name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    faculty = db.Column(db.String(100), nullable=False) # Khoa (Toán, CNTT, Hóa, Sinh...)
    cohort = db.Column(db.String(20), nullable=False)   # Khóa (VD: K67)
    gpa = db.Column(db.Float, default=0.0)

    # Quan hệ với bảng Enrollment (Đăng ký môn học)
    enrollments = db.relationship('Enrollment', backref='student', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    """Bảng Môn học"""
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), unique=True, nullable=False) # Mã môn (VD: MAT1092)
    course_name = db.Column(db.String(150), nullable=False)
    credits = db.Column(db.Integer, nullable=False) # Số tín chỉ
    lecturer = db.Column(db.String(100)) # Giảng viên
    max_students = db.Column(db.Integer, default=60)

    # Quan hệ với bảng Enrollment
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)

class Enrollment(db.Model):
    """Bảng Đăng ký môn học / Điểm (Bảng trung gian n-n)"""
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    semester = db.Column(db.String(20), nullable=False) # Học kỳ (VD: HK1_2025-2026)
    midterm_score = db.Column(db.Float, nullable=True)  # Điểm giữa kỳ
    final_score = db.Column(db.Float, nullable=True)    # Điểm cuối kỳ

    @property
    def total_score(self):
        if self.midterm_score is not None and self.final_score is not None:
            return round((self.midterm_score * 0.4) + (self.final_score * 0.6), 1)
        return None

class News(db.Model):
    """Bảng Thông báo từ nhà trường"""
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.String(100), default='Phòng Đào tạo HUS')

@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))


# ==========================================
# 3. GIAO DIỆN HTML TEMPLATES (MÔ PHỎNG)
# ==========================================
# Ghi chú: Thực tế code này nằm ở file riêng biệt. Mình gán vào biến string để chạy trực tiếp.

HTML_BASE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>HUS Portal - Cổng thông tin sinh viên</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; margin: 0; padding: 0; }
        .header { background-color: #003366; color: white; padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; }
        .nav a { color: white; margin-left: 20px; text-decoration: none; font-weight: bold; }
        .container { width: 80%; margin: 20px auto; background: white; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1); border-radius: 8px; }
        h1, h2, h3 { color: #003366; }
        .alert { padding: 10px; margin-bottom: 15px; border-radius: 4px; }
        .alert-success { background-color: #d4edda; color: #155724; }
        .alert-danger { background-color: #f8d7da; color: #721c24; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        table, th, td { border: 1px solid #ddd; }
        th, td { padding: 10px; text-align: left; }
        th { background-color: #003366; color: white; }
        .btn { padding: 8px 15px; background-color: #28a745; color: white; border: none; cursor: pointer; text-decoration: none; border-radius: 4px; }
        .btn-danger { background-color: #dc3545; }
        .form-group { margin-bottom: 15px; }
        .form-group input { width: 100%; padding: 8px; box-sizing: border-box; }
        .news-card { border-bottom: 1px solid #eee; padding-bottom: 15px; margin-bottom: 15px; }
        .news-date { color: #888; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h2 style="margin: 0; color: white;">Trường Đại học Khoa học Tự nhiên</h2>
            <small>Cổng thông tin sinh viên HUS</small>
        </div>
        <div class="nav">
            {% if current_user.is_authenticated %}
                <span>Xin chào, {{ current_user.full_name }} ({{ current_user.student_code }})</span>
                <a href="{{ url_for('dashboard') }}">Trang chủ</a>
                <a href="{{ url_for('courses') }}">Đăng ký học</a>
                <a href="{{ url_for('grades') }}">Xem điểm</a>
                <a href="{{ url_for('logout') }}">Đăng xuất</a>
            {% else %}
                <a href="{{ url_for('login') }}">Đăng nhập</a>
            {% endif %}
        </div>
    </div>
    
    <div class="container">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        {% block content %}{% endblock %}
    </div>
</body>
</html>
"""

HTML_LOGIN = HTML_BASE.replace('{% block content %}{% endblock %}', """
    <h2>Đăng nhập hệ thống</h2>
    <form method="POST" style="max-width: 400px;">
        <div class="form-group">
            <label>Mã sinh viên:</label>
            <input type="text" name="student_code" required placeholder="Ví dụ: 22001122">
        </div>
        <div class="form-group">
            <label>Mật khẩu:</label>
            <input type="password" name="password" required>
        </div>
        <button type="submit" class="btn">Đăng nhập</button>
    </form>
""")

HTML_DASHBOARD = HTML_BASE.replace('{% block content %}{% endblock %}', """
    <h2>Bảng tin sinh viên</h2>
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
            <h3>Thông tin cá nhân</h3>
            <p><strong>Họ và tên:</strong> {{ current_user.full_name }}</p>
            <p><strong>Mã sinh viên:</strong> {{ current_user.student_code }}</p>
            <p><strong>Khoa:</strong> {{ current_user.faculty }}</p>
            <p><strong>Khóa:</strong> {{ current_user.cohort }}</p>
            <p><strong>GPA Tích lũy:</strong> {{ current_user.gpa }}</p>
        </div>
        <div style="flex: 2;">
            <h3>Thông báo từ nhà trường</h3>
            {% for n in news %}
                <div class="news-card">
                    <h4 style="margin: 0 0 5px 0;">{{ n.title }}</h4>
                    <span class="news-date">Đăng bởi: {{ n.author }} | {{ n.date_posted.strftime('%d/%m/%Y') }}</span>
                    <p>{{ n.content }}</p>
                </div>
            {% else %}
                <p>Không có thông báo mới.</p>
            {% endfor %}
        </div>
    </div>
""")

HTML_COURSES = HTML_BASE.replace('{% block content %}{% endblock %}', """
    <h2>Đăng ký học phần (Học kỳ hiện tại)</h2>
    <h3>Danh sách các môn đang mở</h3>
    <table>
        <tr>
            <th>Mã môn</th>
            <th>Tên môn học</th>
            <th>Tín chỉ</th>
            <th>Giảng viên</th>
            <th>Sĩ số</th>
            <th>Thao tác</th>
        </tr>
        {% for course in available_courses %}
        <tr>
            <td>{{ course.course_code }}</td>
            <td>{{ course.course_name }}</td>
            <td>{{ course.credits }}</td>
            <td>{{ course.lecturer }}</td>
            <td>{{ course.enrollments|length }} / {{ course.max_students }}</td>
            <td>
                <form method="POST" action="{{ url_for('enroll', course_id=course.id) }}" style="display:inline;">
                    <button type="submit" class="btn">Đăng ký</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>

    <h3 style="margin-top: 40px;">Môn học đã đăng ký</h3>
    <table>
        <tr>
            <th>Mã môn</th>
            <th>Tên môn học</th>
            <th>Tín chỉ</th>
            <th>Thao tác</th>
        </tr>
        {% for enr in my_enrollments %}
        <tr>
            <td>{{ enr.course.course_code }}</td>
            <td>{{ enr.course.course_name }}</td>
            <td>{{ enr.course.credits }}</td>
            <td>
                <form method="POST" action="{{ url_for('unenroll', enroll_id=enr.id) }}" style="display:inline;">
                    <button type="submit" class="btn btn-danger">Hủy đăng ký</button>
                </form>
            </td>
        </tr>
        {% else %}
        <tr><td colspan="4">Bạn chưa đăng ký môn nào học kỳ này.</td></tr>
        {% endfor %}
    </table>
""")

HTML_GRADES = HTML_BASE.replace('{% block content %}{% endblock %}', """
    <h2>Kết quả học tập</h2>
    <table>
        <tr>
            <th>Mã môn</th>
            <th>Tên môn học</th>
            <th>Học kỳ</th>
            <th>Tín chỉ</th>
            <th>Điểm giữa kỳ (40%)</th>
            <th>Điểm cuối kỳ (60%)</th>
            <th>Điểm tổng kết</th>
        </tr>
        {% for enr in my_enrollments %}
        <tr>
            <td>{{ enr.course.course_code }}</td>
            <td>{{ enr.course.course_name }}</td>
            <td>{{ enr.semester }}</td>
            <td>{{ enr.course.credits }}</td>
            <td>{{ enr.midterm_score if enr.midterm_score != None else '-' }}</td>
            <td>{{ enr.final_score if enr.final_score != None else '-' }}</td>
            <td><strong>{{ enr.total_score if enr.total_score != None else 'Chưa có' }}</strong></td>
        </tr>
        {% else %}
        <tr><td colspan="7">Chưa có dữ liệu điểm.</td></tr>
        {% endfor %}
    </table>
""")

# ==========================================
# 4. ĐỊNH TUYẾN URL (ROUTES & CONTROLLERS)
# ==========================================

@app.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        student_code = request.form.get('student_code')
        password = request.form.get('password')

        student = Student.query.filter_by(student_code=student_code).first()
        if student and student.check_password(password):
            login_user(student)
            flash(f'Đăng nhập thành công! Chào mừng {student.full_name}.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Mã sinh viên hoặc mật khẩu không chính xác.', 'danger')

    return render_template_string(HTML_LOGIN)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Bạn đã đăng xuất khỏi hệ thống.', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    # Lấy 5 thông báo mới nhất
    recent_news = News.query.order_by(News.date_posted.desc()).limit(5).all()
    return render_template_string(HTML_DASHBOARD, news=recent_news)

@app.route('/courses')
@login_required
def courses():
    # Lấy danh sách môn học sinh viên chưa đăng ký
    enrolled_course_ids = [e.course_id for e in current_user.enrollments]
    available_courses = Course.query.filter(Course.id.notin_(enrolled_course_ids)).all()

    # Lấy danh sách môn đang học
    my_enrollments = Enrollment.query.filter_by(student_id=current_user.id).all()

    return render_template_string(HTML_COURSES, available_courses=available_courses, my_enrollments=my_enrollments)

@app.route('/enroll/<int:course_id>', methods=['POST'])
@login_required
def enroll(course_id):
    course = Course.query.get_or_404(course_id)
    # Kiểm tra sĩ số
    if len(course.enrollments) >= course.max_students:
        flash(f'Lớp {course.course_name} đã đầy!', 'danger')
    else:
        new_enrollment = Enrollment(student_id=current_user.id, course_id=course.id, semester='HK2_2025-2026')
        db.session.add(new_enrollment)
        db.session.commit()
        flash(f'Đăng ký thành công môn {course.course_name}!', 'success')

    return redirect(url_for('courses'))

@app.route('/unenroll/<int:enroll_id>', methods=['POST'])
@login_required
def unenroll(enroll_id):
    enrollment = Enrollment.query.get_or_404(enroll_id)
    if enrollment.student_id == current_user.id:
        db.session.delete(enrollment)
        db.session.commit()
        flash('Đã hủy đăng ký môn học.', 'success')
    return redirect(url_for('courses'))

@app.route('/grades')
@login_required
def grades():
    my_enrollments = Enrollment.query.filter_by(student_id=current_user.id).all()
    return render_template_string(HTML_GRADES, my_enrollments=my_enrollments)


# ==========================================
# 5. KHỞI TẠO DỮ LIỆU MẪU (DUMMY DATA FOR HUS)
# ==========================================
def init_dummy_data():
    """Tạo database và chèn dữ liệu mẫu nếu chưa có"""
    with app.app_context():
        db.create_all()
        if not Student.query.first():
            # 1. Tạo sinh viên mẫu
            sv1 = Student(student_code='22001122', full_name='Nguyễn Văn A', faculty='Toán - Cơ - Tin học', cohort='K67')
            sv1.set_password('hus123')
            sv2 = Student(student_code='23004455', full_name='Trần Thị B', faculty='Hóa học', cohort='K68')
            sv2.set_password('hus123')
            db.session.add_all([sv1, sv2])

            # 2. Tạo môn học mẫu đặc thù HUS
            c1 = Course(course_code='MAT1092', course_name='Giải tích 1', credits=4, lecturer='TS. Lê Văn C')
            c2 = Course(course_code='INT1050', course_name='Nhập môn Công nghệ Thông tin', credits=3, lecturer='PGS.TS Nguyễn D')
            c3 = Course(course_code='PHY1001', course_name='Cơ nhiệt', credits=3, lecturer='TS. Phạm E')
            c4 = Course(course_code='CHE1080', course_name='Hóa học Đại cương', credits=3, lecturer='TS. Vũ F')
            db.session.add_all([c1, c2, c3, c4])

            # 3. Tạo thông báo
            n1 = News(title='Kế hoạch thi cuối kỳ II năm học 2025-2026', content='Sinh viên theo dõi lịch thi chi tiết được cập nhật trên cổng thông tin.')
            n2 = News(title='Thông báo đăng ký chuyên ngành K67', content='Khoa Toán - Cơ - Tin học thông báo thời gian đăng ký chuyên ngành từ 15/04/2026.')
            db.session.add_all([n1, n2])

            db.session.commit()
            print("Đã khởi tạo Database và dữ liệu mẫu thành công!")

# ==========================================
# 6. KHỞI CHẠY SERVER
# ==========================================
if __name__ == '__main__':
    # Tạo dữ liệu giả lập ban đầu để test
    init_dummy_data()
    # Chạy server ở chế độ debug
    print("Truy cập http://127.0.0.1:5000 để xem web.")
    print("Tài khoản test: 22001122 / Mật khẩu: hus123")
    app.run(debug=True)