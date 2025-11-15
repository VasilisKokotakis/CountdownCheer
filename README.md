# CountdownCheer Web App

A small Python project to count down the days, hours, and minutes until Christmas **and any other holidays you add**.
This project includes a **web UI** built with Flask and festive animations.

---

## Features

* Real-time countdown for multiple holidays: Christmas, New Year, Easter (approximate), and user-added holidays.
* Dark-themed, festive web interface with **glowing cards** and **hover sparkles**.
* **Falling snow animation** for a winter holiday feel.
* Add your own custom holidays via a simple form - appear instantly in the countdown.
* **Mobile-friendly responsive design** - cards and forms adjust to any screen size.

---

## Screenshots

**Web Version**
<img width="1500" height="752" alt="image" src="https://github.com/user-attachments/assets/25aa05bc-2d6c-4223-b45f-87e2bce69f28" />

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/VasilisKokotakis/CountdownCheer.git
cd CountdownCheer
```

2. **Install dependencies**

```bash
pip install flask
```

3. **Run the app**

```bash
python main.py
```

4. **Open in your browser**
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to see the countdown.

---

## Project Structure

```
CountdownCheer/
│
├── main.py          # Flask app
├── templates/
│   └── index.html   # HTML template
└── static/
    ├── style.css    # CSS styles
    └── countdown.js # Real-time countdown logic
```

---

## Planned Features (Coming Soon)

* Persistent storage for user-added holidays (JSON or database).
* Animated Santa or holiday lights.
* Optional festive music or sound effects.
* More holiday-themed animations and interactivity.

---

## Technologies Used

* Python 3
* Flask (Web UI)
* HTML/CSS (Web UI)
* JavaScript for **real-time countdown** and **animations**
* `datetime` for countdown calculations

---

## Contributing

Feel free to fork, suggest improvements, or submit pull requests!
This project is perfect for adding **festive features** or experimenting with **Python web apps**.

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

