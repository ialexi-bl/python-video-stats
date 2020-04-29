from .tables import get_results


def choose_best():
    first, second = get_results()
    ans = []
    print(len(first), len(second))
    for i in range(len(first)):
        if (
            (second[i] is None or second[i]["orientation"] == "Г")
            and (
                first[i] is None
                or (
                    first[i]["duration"] > 2
                    and (first[i]["width"] / first[i]["height"] == 16 / 9)
                    and first[i]["fps"] > 20
                )
            )
            # and second[i]["unfocused"] == "нет"
            # and second[i]["sound"] == "нет"
            # and second[i]["rotated"] == "нет"
        ):
            ans.append(first[i]["name"])
    return ans
