# 어떻게 python에게 class를 string으로 보여줄 수 있을까?
# ㄴ> django  model을 포함한 모든 class에는 class가 string으로 보여지게 커스터마이징 할 수 있는 메서드가 있다.
"""
    def __str__(self) -> str:
        return self.name
"""


"""
    class Meta:
        verbose_name_plural = "Amenities"
"""

"""
    readonly_fields = (
        "created_at",
        "updated_at",
    )
"""
