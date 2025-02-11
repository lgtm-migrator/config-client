from cleo import Application

from config import __version__
from config.cli import ConfigClientCommand, DecryptCommand, EncryptCommand

application = Application("config-client", f"{__version__}")
application.add(ConfigClientCommand())
application.add(EncryptCommand())
application.add(DecryptCommand())


if __name__ == "__main__":
    application.run()
