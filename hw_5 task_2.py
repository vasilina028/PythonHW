def calc_mse(act, pred):
    if len(act) != len(pred):
        raise ValueError("Длины списков фактических и прогнозных значений должны быть одинаковыми.")

    squared_errors = [(y_act - y_p) ** 2 for y_act, y_p in zip(act, pred)]
    mse = sum(squared_errors) / len(act)

    return mse

act_vals = [10, 15, 12, 8, 14]
pred_vals = [12, 13, 11, 9, 13]

mse = calc_mse(act_vals, pred_vals)
print(f"{mse:.2f}")