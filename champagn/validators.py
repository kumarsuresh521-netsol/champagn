from django.core.exceptions import ValidationError

def validate_category_image(self):
    if self.size > 100*1024:
        raise ValidationError("Image file too large ( > 100kb )")
    return True


def validate_product_image(self):
    if self.size > 300*1024:
        raise ValidationError("Image file too large ( > 300kb )")
    return True
