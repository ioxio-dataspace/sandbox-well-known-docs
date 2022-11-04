from pathlib import Path

from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):
    SRC_PATH: Path = Path(__file__).parent / "src"
    SCHEMAS_PATH: Path = Path(__file__).parent / "schemas"
    HTML_PATH: Path = Path(__file__).parent / "html"

    DATASPACE_BASE_DOMAIN: str = "sandbox.ioxio-dataspace.com"
    AUTHENTICATION_PROVIDER_URL: HttpUrl = "https://login.sandbox.ioxio-dataspace.com"
    CONSENT_PROVIDER_URL: HttpUrl = "https://consent.sandbox.ioxio-dataspace.com"
    WEBSITE_URL: HttpUrl = "https://sandbox.ioxio-dataspace.com"
    DATASPACE_DOCS_URL: HttpUrl = "https://docs.sandbox.ioxio-dataspace.com"
    DEFINITIONS_VIEWER_URL: HttpUrl = "https://definitions.sandbox.ioxio-dataspace.com"
    DEVELOPER_PORTAL_URL: HttpUrl = "https://developer.sandbox.ioxio-dataspace.com"
    PRODUCT_GATEWAY_URL: HttpUrl = "https://gateway.sandbox.ioxio-dataspace.com"
    DEFINITIONS_GIT_URL: HttpUrl = (
        "https://github.com/ioxio-dataspace/sandbox-definitions.git"
    )
    DEFINITIONS_WEB_URL: HttpUrl = (
        "https://github.com/ioxio-dataspace/sandbox-definitions"
    )


conf = Settings()
