from .tables import get_results


def choose_best():
    first, second = get_results()
    ans = []
    print(len(first), len(second))
    for i in range(len(first)):
        if (
            (
                second[i] is None
                or second[i]["orientation"] is None
                or second[i]["orientation"] == "Г"
            )
            and (
                first[i] is None
                or (
                    (first[i]["duration"] is None or first[i]["duration"] > 2)
                    and (
                        first[i]["width"] is None
                        or first[i]["height"] is None
                        or (first[i]["width"] / first[i]["height"] == 16 / 9)
                    )
                    and (first[i]["fps"] is None or first[i]["fps"] > 25)
                )
            )
            and second[i]["unfocused"] == "нет"
        ):
            ans.append(first[i]["name"])
    return ans
