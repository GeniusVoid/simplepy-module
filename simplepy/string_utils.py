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

        # DICTIONARY (search keys and values)
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

        else:
            msg = "TypeError: unsupported container type"
            print(msg)
            return msg

    except TypeError as e:
        msg = f"TypeError: {e}"
        print(msg)
        return msg

    except ValueError as e:
        msg = f"ValueError: {e}"
        print(msg)
        return msg

    except IndexError as e:
        msg = f"IndexError: {e}"
        print(msg)
        return msg

    except KeyError as e:
        msg = f"KeyError: {e}"
        print(msg)
        return msg

    except AttributeError as e:
        msg = f"AttributeError: {e}"
        print(msg)
        return msg

    except Exception:
        # Unknown error → silent safe fallback
        return -1