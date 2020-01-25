#!/usr/bin/env python

#from cpt.packager import ConanMultiPackager

#if __name__ == "__main__":
#    builder = ConanMultiPackager(username="altairwei", archs=["x86_64"], build_policy="missing")
#    builder.add_common_builds(pure_c=False)
#    builder.run()

from bincrafters import build_template_default

if __name__ == "__main__":

    builder = build_template_default.get_builder()
    builder.run()