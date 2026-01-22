const languageData = {
    'IT': {
        hello: "Ciao! 👋",
        thank_you: "Grazie! 🙏",
        cheers: "Salute! 🍷"
    },
    'FR': {
        hello: "Bonjour! 👋",
        thank_you: "Merci! 🙏",
        cheers: "Santé! 🥂"
    },
    'ES': {
        hello: "Hola! 👋",
        thank_you: "Gracias! 🙏",
        cheers: "Salud! 🍻"
    },
    'DE': {
        hello: "Hallo! 👋",
        thank_you: "Danke! 🙏",
        cheers: "Prost! 🍻"
    },
    'JP': {
        hello: "Konnichiwa! 👋",
        thank_you: "Arigato! 🙏",
        cheers: "Kanpai! 🍶"
    },
    'CN': {
        hello: "Ni Hao! 👋",
        thank_you: "Xie Xie! 🙏",
        cheers: "Ganbei! 🍵"
    },
    'PT': {
        hello: "Olá! 👋",
        thank_you: "Obrigado! 🙏",
        cheers: "Saúde! 🍷"
    },
    'GR': {
        hello: "Yassas! 👋",
        thank_you: "Efcharisto! 🙏",
        cheers: "Yamas! 🥃"
    },
    'TR': {
        hello: "Merhaba! 👋",
        thank_you: "Teşekkürler! 🙏",
        cheers: "Şerefe! 🦁"
    },
    'RU': {
        hello: "Privet! 👋",
        thank_you: "Spasibo! 🙏",
        cheers: "Na Zdorovie! 🍸"
    },
    'BG': {
        hello: "Zdravey! 👋",
        thank_you: "Blagodarya! 🙏",
        cheers: "Nazdrave! 🍻"
    },
    'GB': {
        hello: "Hello! 👋",
        thank_you: "Cheers! 🙏",
        cheers: "Cheers! 🍻"
    },
    'US': {
        hello: "Hello! 👋",
        thank_you: "Thank you! 🙏",
        cheers: "Cheers! 🍻"
    }
};

function renderLanguageGuide(countryCode) {
    const container = document.getElementById('language-guide-container');
    if (!container) return;

    if (['US', 'GB', 'AU', 'NZ', 'CA'].includes(countryCode)) {
        container.innerHTML = `
            <div class="info-card language-card" style="border-left: 5px solid #28a745;">
                <h3>🗣️ Language Guide</h3>
                <div class="language-content">
                    <p style="font-size: 1.1rem; margin: 0;">Local Language: <strong>English</strong></p>
                    <p class="text-muted" style="margin-top: 0.5rem;">You're good to go! No translation needed here. 😎</p>
                </div>
            </div>
        `;
        return;
    }

    const data = languageData[countryCode] || {
        hello: "Hello! 👋",
        thank_you: "Thank you! 🙏",
        cheers: "Cheers! 🍻"
    };

    container.innerHTML = `
        <div class="info-card language-card">
            <h3 style="display: flex; align-items: center; gap: 0.5rem;">
                🗣️ Survival Guide
                <span class="badge bg-secondary" style="font-size: 0.7em; margin-left: auto;">${countryCode}</span>
            </h3>
            <div class="language-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem; text-align: center;">
                <div class="lang-item">
                    <div class="lang-icon" style="font-size: 1.5rem; margin-bottom: 0.5rem;">👋</div>
                    <div class="lang-label" style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-secondary);">Hello</div>
                    <div class="lang-phrase" style="font-weight: bold; font-size: 1.1rem; color: var(--text-primary);">${data.hello}</div>
                </div>
                <div class="lang-item">
                    <div class="lang-icon" style="font-size: 1.5rem; margin-bottom: 0.5rem;">🙏</div>
                    <div class="lang-label" style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-secondary);">Thanks</div>
                    <div class="lang-phrase" style="font-weight: bold; font-size: 1.1rem; color: var(--text-primary);">${data.thank_you}</div>
                </div>
                <div class="lang-item">
                    <div class="lang-icon" style="font-size: 1.5rem; margin-bottom: 0.5rem;">🥂</div>
                    <div class="lang-label" style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-secondary);">Cheers</div>
                    <div class="lang-phrase" style="font-weight: bold; font-size: 1.1rem; color: var(--text-primary);">${data.cheers}</div>
                </div>
            </div>
        </div>
    `;
}
