from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=254, null=False)
    age = models.IntegerField(null=False)
    money = models.IntegerField(null=False, default=0)
    salary = models.IntegerField() 
    financial_products = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # profile_img = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)

    

# 포트폴리오
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_bank = models.CharField(max_length=50)
    

# 정기 예금 baseinfo
class DepositProductBaseinfo(models.Model):
    # 상품목록 - 상품 - 기본정보
    dcls_month = models.CharField(max_length=10) # 공시 제출월 [YYYYMM]
    fin_co_no = models.CharField(max_length=100) # 금융회사 코드
    kor_co_nm = models.CharField(max_length=100) # 금융회사 명
    fin_prdt_cd = models.CharField(max_length=100) # 금융상품 코드
    fin_prdt_nm = models.CharField(max_length=150) # 금융상품 명
    join_way = models.TextField() # 가입 방법
    mtrt_int = models.TextField() # 만기 후 이자율
    spcl_cnd = models.TextField() # 우대조건
    join_deny =  models.IntegerField() # 가입제한 1:제한없음, 2:서민전용, 3:일부제한
    join_member = models.CharField(max_length=300) # 가입대상
    etc_note = models.TextField() # 기타 유의사항
    max_limit = models.IntegerField(null=True) # 최고한도
    dcls_strt_day = models.CharField(max_length=10) # 공시 시작일
    dcls_end_day = models.CharField(max_length=10, null=True) # 공시 종료일
    fin_co_subm_day = models.CharField(max_length=15) # 금융회사 제출일 [YYYYMMDDHH24MI]
    
# 정기 예금 options  
class DepositProductOption(models.Model):    
    # 옵션 목록 - 옵션
    fin_prdt_cd = models.ForeignKey(DepositProductBaseinfo, on_delete=models.CASCADE, related_name="") # 금융상품 코드
    intr_rate_type = models.CharField(max_length=10) # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=10) # 저축 금리 유형명
    save_trm = models.IntegerField() # 저축 기간 [단위: 개월]
    intr_rate = models.FloatField(null=True) # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField() # 최고 우대금리 [소수점 2자리]


# 적금 baseinfo
class SavingProductBaseinfo(models.Model):
    dcls_month = models.CharField(max_length=10) # 공시 제출월 [YYYYMM]
    fin_co_no  = models.CharField(max_length=100) # 금융회사 코드
    kor_co_nm  = models.CharField(max_length=100) # 금융회사 명
    fin_prdt_cd  = models.CharField(max_length=100) # 금융상품 코드
    fin_prdt_nm  = models.CharField(max_length=150) # 금융 상품명
    join_way  = models.TextField() # 가입 방법
    mtrt_int  = models.TextField() # 만기 후 이자율
    spcl_cnd  = models.TextField() # 우대조건
    join_deny  = models.IntegerField() # 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_member  = models.CharField(max_length=300) # 가입대상
    etc_note  = models.TextField() # 기타 유의사항
    max_limit  = models.IntegerField() # 최고한도
    dcls_strt_day  = models.TextField() # 공시 시작일
    dcls_end_day  = models.TextField() # 공시 종료일
    fin_co_subm_day	= models.TextField() # 금융회사 제출일 [YYYYMMDDHH24MI]

# 적금 options
class SavingProductOption(models.Model):
    intr_rate_type = models.TextField() # 저축 금리 유형
    intr_rate_type_nm = models.TextField() # 저축 금리 유형명
    rsrv_type = models.TextField() # 적립 유형
    rsrv_type_nm = models.CharField(max_length=10) # 적립 유형명
    save_trm = models.IntegerField() # 저축 기간 [단위: 개월]
    intr_rate =models.FloatField() # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField() # 최고 우대금리 [소수점 2자리]

# 커뮤니티 게시글
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.IntegerField()
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(User, related_name="likeposts")

# 커뮤니티 댓글
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

