import sentry_sdk
from controllers.main_menu import MainMenuController
from dotenv import load_dotenv
import os


if __name__ == "__main__":
    load_dotenv()
    sentry_dsn = os.getenv("SENTRY_DSN")
    sentry_sdk.init(
        dsn=sentry_dsn,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )
    controller = MainMenuController()
    controller.display_menu()
