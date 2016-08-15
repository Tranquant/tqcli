import optparse
import os
import sys

from tqcli.config.config import TQ_API_ROOT_URL, logger
from tqcli.batch.server_handler import TranQuant


def main():
    usage = open(os.path.join(sys.path[0], 'README.md'), 'r').read()
    parser = optparse.OptionParser(usage)
    parser.add_option(
        '-i', '--input',
        dest='input_path',
        default='',
        help='Path to the input file(s).',
    )

    parser.add_option(
        "-t", "--token",
        dest='token',
        default='',
        help='Authentication token.',
    )

    parser.add_option(
        "-d", "--datasource-id",
        dest='datasource_id',
        default='',
        help='DataSource ID.',
    )

    parser.add_option(
        "-s", "--dataset-id",
        dest='dataset_id',
        default='',
        help='DataSet ID.',
    )

    options, remainder = parser.parse_args()

    tq = TranQuant(
        root_url=TQ_API_ROOT_URL,
        token=options.token,
        datasource_id=options.datasource_id,
        dataset_id=options.dataset_id
    )
    try:
        tq.upload(input_path=options.input_path)
    except Exception as ex:
        logger.exception(ex)
        logger.error(ex)

if __name__ == '__main__':
    main()
