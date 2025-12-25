def xfind(container, target):
    try:
        # STRING, LIST, TUPLE
        if isinstance(container, (str, list, tuple)):
            indexes = []

            for i in range(len(container)):
                if container[i] == target:
                    indexes.append(i)

            if len(indexes) == 0:
                return -1
            elif len(indexes) == 1:
                return indexes[0]
            else:
                return indexes

        # DICTIONARY (search keys, then values)
        elif isinstance(container, dict):
            results = []

            for key, value in container.items():
                if key == target or value == target:
                    results.append(key)

            if len(results) == 0:
                return -1
            elif len(results) == 1:
                return results[0]
            else:
                return results

        # SET
        elif isinstance(container, set):
            if target in container:
                return target
            else:
                return -1

        # UNSUPPORTED TYPE
        else:
            return -1

    except Exception:
        # ABSOLUTE SAFETY: never raise error
        return -1
