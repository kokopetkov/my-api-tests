from pydantic import BaseModel, ConfigDict

class MyBaseModel(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
        str_strip_whitespace=True,  # Автоматично маха разстояния в началото/края на стрингове
        validate_assignment=True   # Валидира данните дори ако ги променяш ръчно по-късно
    )
