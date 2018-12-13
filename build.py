from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="altairwei", gcc_versions=["7"],
        archs=["x86_64"], build_policy="missing")
    builder.add_common_builds(pure_c=False)
    builder.run()