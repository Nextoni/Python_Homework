def slope_style_score(scores):
    result = 0
    scores.sort()
    new_scores = scores[1:-1]

    for sc in new_scores:
        result = result + sc
    
    result = result / len(new_scores)

    result = str(result)
    result = result[0:result.count(".") + 4]
    result = float(result)

    return result

print(slope_style_score([94, 95, 95, 95, 90]))