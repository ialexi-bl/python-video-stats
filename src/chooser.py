from .tables import get_results


def choose_best():
    first, second = get_results()
    ans = []
    print(len(first), len(second))
    for i in range(len(first)):
        if (
            second[i]["orientation"] == "Г"
            and first[i]["duration"] > 2
            and (first[i]["width"] / first[i]["higth"] == 16 / 9)
            and first[i]["fps"] > 25
            and second[i]["unfocused"] == "нет"
            and second[i]["sound"] == "нет"
            and second[i]["rotated"] == "нет"
        ):
            ans.append(first[i]["name"])
    return ans
