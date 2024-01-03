# Article 모델의 데이터를 만들어 주는 명령어

from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from articles.models import Article

from faker import Faker
import random

class Command(BaseCommand):
    help = "Article 데이터를 생성하는 명령어"

    # 명령어 옵션 추가
    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--number",
            default=10,
            type=int,
            help="인스턴스를 몇개 생성할 것인가?"
        )

    # 이 명령어가 동작하는 코드를 handle 함수에 작성
    def handle(self, *args: Any, **options: Any):
        number = options.get("number") # 위에서 작성한 옵션값을 가져온다.
        users = get_user_model().objects.all() # Article을 작성한 유저는 있다고 가정함

        # 가짜 데이터를 생성해주는 Faker 객체 생성
        fake = Faker(["ko_KR"])

        # number개의 Article 인스턴스 만들기
        for i in range(number):
            user = random.choice(users) # 전체 유저 중에서 랜덤으로 하나 뽑기
            article = Article.objects.create(user=user, title=fake.bs(),content=fake.paragraph(nb_sentences=5))

        # 터미널에 메세지 출력하기
        self.stdout.write(self.style.SUCCESS(f"{number}개의 Article이 생성되었습니다."))