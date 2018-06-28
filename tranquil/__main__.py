import sys
from os.path import dirname

from .application import make_app, cli
from .handler import get_tranquilized_functions


def main():
    args = cli().parse_args()

    sys.path.append(dirname(args.filename))
    functions = get_tranquilized_functions(args.filename)
    app = make_app(functions)

    app.run(host=args.anaconda_project_address, port=args.anaconda_project_port)

if __name__ == '__main__':
    main()
