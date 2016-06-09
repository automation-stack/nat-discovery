import argparse
import logging
import sys
import time
from termcolor import colored
from json import dumps

import discovery


def make_argument_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='enable debug logging'
    )
    parser.add_argument(
        '-j', '--json', action='store_true',
        default=False,
        help='JSON output'
    )
    parser.add_argument(
        '-e', '--exit', action='store_true',
        default=False,
        help='exit on complete (by default sleep)'
    )
    parser.add_argument(
        '-H', '--stun-host',
        help='STUN host to use'
    )
    parser.add_argument(
        '-P', '--stun-port', type=int,
        default=discovery.DEFAULTS['stun_port'],
        help='STUN host port to use'
    )
    parser.add_argument(
        '-i', '--source-ip',
        default=discovery.DEFAULTS['source_ip'],
        help='network interface for client'
    )
    parser.add_argument(
        '-p', '--source-port', type=int,
        default=discovery.DEFAULTS['source_port'],
        help='port to listen on for client'
    )
    parser.add_argument(
        '--version', action='version', version=discovery.__version__
    )
    return parser


def main():
    try:
        options = make_argument_parser().parse_args()

        def fprint(msg):
            if not options.json:
                print msg
            return

        logging.basicConfig(format='- %(asctime)-15s %(message)s')
        discovery.log.setLevel(
            options.debug and not options.json
            if logging.DEBUG else logging.INFO
        )

        fprint('{}'.format(colored(
            '- Discovering NAT type (it may take 5 to 60 seconds) ...',
            'cyan'
        )))
        nat_type, external_ip, external_port = discovery.get_ip_info(
            source_ip=options.source_ip,
            source_port=options.source_port,
            stun_host=options.stun_host,
            stun_port=options.stun_port
        )
        fprint('{}\n'.format('-' * 60))
        fprint(colored('\tNAT Type: {}'.format(nat_type), 'magenta'))
        fprint('\tExternal IP: {}'.format(external_ip))
        fprint('\tExternal Port: {}'.format(external_port))
        fprint('\n{}'.format(('-' * 60)))

        if options.json:
            print dumps({
                'type': nat_type,
                'external_ip': external_ip,
                'external_port': external_port
            }, indent=4)

        if not options.exit:
            try:
                while True:
                    time.sleep(1000)
            except KeyboardInterrupt:
                pass

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
