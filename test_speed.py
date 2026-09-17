import argparse

from src.ad_robot_test.DownloadTestService import DownloadPictureTestService

parser = argparse.ArgumentParser("speed_test")
parser.add_argument('-c', '--chunk', help="Download chunk size", type=int)
parser.add_argument('-u', '--url', help="Url link", type=str)
parser.add_argument('-i', '--iterations', help="Iterations count", type=int)
args = parser.parse_args()
print(
    'Your internet speed is {} bytes per second'.format(
        DownloadPictureTestService(url=args.url, chunk=args.chunk, iterations=args.iterations).speed
    )
)
