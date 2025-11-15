function updateCountdowns() {
    document.querySelectorAll("[data-month]").forEach(card => {
        const month = parseInt(card.dataset.month);
        const day = parseInt(card.dataset.day);

        const now = new Date();
        let target = new Date(now.getFullYear(), month - 1, day, 0, 0, 0);

        if (target < now) {
            target = new Date(now.getFullYear() + 1, month - 1, day, 0, 0, 0);
        }

        const diff = target - now;

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((diff / (1000 * 60)) % 60);
        const seconds = Math.floor((diff / 1000) % 60);

        card.querySelector(".time").textContent =
            `${days}d ${hours}h ${minutes}m ${seconds}s`;
    });
}

setInterval(updateCountdowns, 1000);
updateCountdowns();
