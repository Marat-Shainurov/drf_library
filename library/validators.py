from django.core import validators


class ISBNValidator(validators.RegexValidator):
    """
    Checks whether a provided string representing the Book's ISBN aligns with the regular expression pattern.
    All the ISBNs should contain digits and '-' characters only.
    """
    regex = r"^[\d-]+$"
    message = "Enter a valid ISBN. This value may contain only digits and '-' characters"


class PublishYearValidator(validators.RegexValidator):
    """
    Checks whether a provided string representing the Book's publish_year aligns with the regular expression pattern.
    All the publish_years should contain from 1 to 4 digits only.
    """
    regex = r"^\d{1,4}$"
    message = "Enter a valid 4-digit publish year."
