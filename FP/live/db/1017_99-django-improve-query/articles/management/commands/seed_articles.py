# aricle model의 데이터를 만들어주는 명령어

from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from articles.models import Article
import random
from faker import Faker

class Command(BaseCommand):
    help = "Article 데이터 생성하는 명령어"
    
    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--number",
            default=10,
            type=int,
            help="인스턴스를 몇 개 생성할 것인가"
        )
    
    # 이 명령어가 동작하는코드를 handle 함수에 작성
    def handle(self, *args: Any, **options: Any):
        number = options.get("number") # 위에서 작성한 옵션값을 가져온다
        users = get_user_model().objects.all()
        
        # 가짜 데이터를 생성해주는 Faker 객체 생성
        fake = Faker(["ko_KR"])
        
         # number개의 Article 인스턴스 만들기
        for i in range(number):
            user = random.choice(users)
            article = Article.objects.create(user=user, title=fake.bs(), content=fake.paragraph(nb_sentences=5))

        # 터미널에 메시지 출력하기
        self.stdout.write(self.style.SUCCESS(f"{number}개의 Article이 생성되었습니당"))
                