# Generated by Django 4.2.17 on 2025-01-08 09:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[("manager", "หัวหน้า"), ("employee", "พนักงาน")],
                        max_length=10,
                        verbose_name="ตำแหน่ง",
                    ),
                ),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("purchasing", "ฝ่ายจัดซื้อ"),
                            ("sale_co", "ฝ่ายSaleCo"),
                            ("store", "ฝ่ายสโตร์"),
                            ("delivery", "ฝ่ายจัดส่ง"),
                            ("accounting", "ฝ่ายบัญชี"),
                            ("engineering", "ฝ่ายวิศวะ"),
                            ("it", "ฝ่ายIT"),
                            ("gps", "ฝ่ายGPS"),
                            ("production", "ฝ่ายผลิต"),
                            ("sales_project", "ฝ่ายSales Project"),
                            ("sales", "ฝ่ายSales"),
                            ("marketing", "ฝ่ายการตลาด"),
                            ("hr", "ฝ่ายHR"),
                            ("sales_solar", "ฝ่ายSales Solar Project"),
                            ("sales_plusclean", "ฝ่ายSales Plusclean Project"),
                        ],
                        max_length=20,
                        verbose_name="แผนก",
                    ),
                ),
                (
                    "phone",
                    models.CharField(max_length=10, verbose_name="เบอร์โทรศัพท์"),
                ),
                ("address", models.TextField(verbose_name="ที่อยู่")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "ผู้ใช้งาน",
                "verbose_name_plural": "ผู้ใช้งาน",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="LocationSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="ชื่อสถานที่")),
                (
                    "latitude",
                    models.DecimalField(
                        decimal_places=15, max_digits=20, verbose_name="ละติจูด"
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        decimal_places=15, max_digits=20, verbose_name="ลองจิจูด"
                    ),
                ),
                (
                    "radius",
                    models.IntegerField(default=100, verbose_name="รัศมี (เมตร)"),
                ),
            ],
            options={
                "verbose_name": "ตั้งค่าพิกัดสถานที่",
                "verbose_name_plural": "ตั้งค่าพิกัดสถานที่",
            },
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="วันที่")),
                (
                    "check_in",
                    models.TimeField(blank=True, null=True, verbose_name="เวลาเข้างาน"),
                ),
                (
                    "check_out",
                    models.TimeField(blank=True, null=True, verbose_name="เวลาออกงาน"),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True,
                        decimal_places=6,
                        max_digits=9,
                        null=True,
                        verbose_name="ละติจูด",
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True,
                        decimal_places=6,
                        max_digits=9,
                        null=True,
                        verbose_name="ลองจิจูด",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("present", "มาทำงาน"),
                            ("late", "มาสาย"),
                            ("absent", "ขาดงาน"),
                            ("leave", "ลา"),
                        ],
                        max_length=10,
                        verbose_name="สถานะ",
                    ),
                ),
                ("note", models.TextField(blank=True, verbose_name="หมายเหตุ")),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="พนักงาน",
                    ),
                ),
            ],
            options={
                "verbose_name": "การลงเวลา",
                "verbose_name_plural": "การลงเวลา",
            },
        ),
    ]
