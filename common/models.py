from django.db import models

# db에 추가하지 않을 model이 있다. -> 다른 model에서 재사용하기 위한 model이다.


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 이 class는 Django에서 model을 configure 할 때 사용한다.
    # abstract = True -> Django가 model을 봐도 DB에 추가하지 않는 옵션 -> 다른 어플리케이션의 models에서 import 후 재사용 가능
    class Meta:
        abstract = True
