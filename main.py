import sys
import os

soran_dir = os.path.join("soran")

sys.path.append(soran_dir)


if __name__ == "__main__":
    from soran.main import main
    main()
