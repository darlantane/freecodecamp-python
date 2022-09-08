def get_days_later(days):
    if days == 1:
        return "(next day)"
    elif days > 1:
        return f"({days} days later)"
    return ""

def add_time(debut, duration, day=False) :

    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    days_later = 0
    one_day = 24
    half_day = 12
    hours, mins = debut.split(":")
    mins, period = mins.split(" ")
    h, m = duration.split(":")

    hours = int(hours)
    mins = int(mins)
    h = int(h)
    m = int(m)
    period = period.strip().lower()

    total_mins = mins + m
    total_hours = hours + h

    if total_mins >= 60:
        total_hours = total_hours + int(total_mins / 60)
        total_mins = int(total_mins % 60)

        if total_mins >= 60:
            total_hours += int(total_mins / 60)
            total_mins = int(total_mins % 60)

    if h or m:
        if period == "pm" and total_hours > half_day:

            if total_hours % one_day >= 1.0:
                days_later += 1

        if total_hours >= half_day:
            hours_left = total_hours / one_day
            days_later = days_later + int(hours_left)

        while True:

            if total_hours < half_day:
                break
            if total_hours >= half_day:
                if period == "am":
                    period = "pm"
                elif period == "pm":
                    period = "am"
                total_hours -= half_day

    remaining_hours = int(total_hours % half_day) or hours + 1
    remaining_mins = int(total_mins % 60)

    results = f'{remaining_hours}:{remaining_mins:02} {period.upper()}'
    if day:
        day = day.strip().lower()
        selected_day = int((week_days.index(day) + days_later) % 7)
        current_day = week_days[selected_day]
        results += f', {current_day.title()} {get_days_later(days_later)}'

    else:
        results = " ".join((results, get_days_later(days_later)))

    return results.strip()