import argparse
from PIL import Image

from tool.predictor import Predictor
from tool.config import Cfg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--img", required=True, help="foo help")
    parser.add_argument("--config", required=True, help="foo help")

    args = parser.parse_args()
    config = Cfg.load_config_from_file(args.config)

    detector = Predictor(config)

    img = Image.open(args.img)
    s = detector.predict(img,return_prob=True)
    print(s)


if __name__ == "__main__":
    main()
