document.addEventListener('DOMContentLoaded', () => {
    // --- Application State ---
    let certifications = [];
    let currentCert = null;
    let currentQuestionIndex = 0;
    let selectedOptionIndex = null;
    let score = 0;
    let currentProvider = null; // Track chosen provider

    const providers = {
        'google-cloud': { name: 'Google Cloud', icon: '☁️', desc: 'Google Cloud Platform professional exam preparation.' },
        'aws': { name: 'AWS', icon: '🍊', desc: 'Amazon Web Services cloud computing certifications.' },
        'dbt': { name: 'dbt', icon: '🛠️', desc: 'dbt Analytics Engineering modeling & engineering tests.' },
        'microsoft': { name: 'Microsoft', icon: '🔷', desc: 'Microsoft Azure cloud platform technologies.' }
    };

    // --- DOM Elements ---
    // Views
    const dashboardView = document.getElementById('dashboard-view');
    const quizView = document.getElementById('quiz-view');
    const scorecardView = document.getElementById('scorecard-view');

    // Header & Global
    const headerLogoBtn = document.getElementById('header-logo-btn');
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    const themeIcon = themeToggleBtn.querySelector('.theme-icon');

    // Dashboard
    const certificationsGrid = document.getElementById('certifications-grid');
    const dashboardLoading = document.getElementById('dashboard-loading');
    const dashboardTitle = dashboardView.querySelector('.view-header h1');
    const dashboardSubtitle = dashboardView.querySelector('.view-header .subtitle');

    // Quiz View
    const backToDashboardBtn = document.getElementById('back-to-dashboard-btn');
    const quizProgressText = document.getElementById('quiz-progress-text');
    const quizProgressBar = document.getElementById('quiz-progress-bar');
    const questionText = document.getElementById('question-text');
    const quizForm = document.getElementById('quiz-form');
    const optionsContainer = document.getElementById('options-container');
    const submitAnswerBtn = document.getElementById('submit-answer-btn');
    const nextQuestionBtn = document.getElementById('next-question-btn');
    
    // Feedback Card
    const feedbackCard = document.getElementById('feedback-card');
    const feedbackStatusIcon = document.getElementById('feedback-status-icon');
    const feedbackStatusTitle = document.getElementById('feedback-status-title');
    const explanationText = document.getElementById('explanation-text');

    // Scorecard View
    const scorecardBadge = document.getElementById('scorecard-badge');
    const scorecardCertName = document.getElementById('scorecard-cert-name');
    const scorePercentage = document.getElementById('score-percentage');
    const scoreFraction = document.getElementById('score-fraction');
    const resultEvaluationCard = document.getElementById('result-evaluation-card');
    const resultStatusTitle = document.getElementById('result-status-title');
    const resultStatusMessage = document.getElementById('result-status-message');
    const retryQuizBtn = document.getElementById('retry-quiz-btn');
    const returnDashboardBtn = document.getElementById('return-dashboard-btn');

    // --- Theme Management ---
    const initTheme = () => {
        const savedTheme = localStorage.getItem('theme') || 'dark';
        if (savedTheme === 'light') {
            document.body.classList.add('light-theme');
            themeIcon.textContent = '☀️';
        } else {
            document.body.classList.remove('light-theme');
            themeIcon.textContent = '🌙';
        }
    };

    themeToggleBtn.addEventListener('click', () => {
        const isLight = document.body.classList.toggle('light-theme');
        if (isLight) {
            themeIcon.textContent = '☀️';
            localStorage.setItem('theme', 'light');
        } else {
            themeIcon.textContent = '🌙';
            localStorage.setItem('theme', 'dark');
        }
    });

    // --- View Routing Helpers ---
    const switchView = (viewName) => {
        // Fade out active views, then show the target view
        const views = [dashboardView, quizView, scorecardView];
        views.forEach(view => {
            if (view.classList.contains('active')) {
                view.classList.remove('active');
            }
        });

        setTimeout(() => {
            if (viewName === 'dashboard') {
                dashboardView.classList.add('active');
            } else if (viewName === 'quiz') {
                quizView.classList.add('active');
            } else if (viewName === 'scorecard') {
                scorecardView.classList.add('active');
            }
        }, 150); // slight delay to allow smooth fade out/in
    };

    // --- Fetch APIs ---
    const fetchCertifications = async () => {
        try {
            dashboardLoading.classList.remove('hidden');
            const response = await fetch('/api/certifications');
            if (!response.ok) throw new Error('Failed to load certifications');
            
            certifications = await response.ok ? await response.json() : [];
            renderDashboard();
        } catch (error) {
            console.error('Error fetching certifications:', error);
            certificationsGrid.innerHTML = `
                <div class="error-alert" style="grid-column: 1/-1; text-align: center; padding: 20px;">
                    <p style="color: var(--error); font-weight: 600;">Failed to load certification lists. Please try again later.</p>
                </div>
            `;
        } finally {
            dashboardLoading.classList.add('hidden');
        }
    };

    const loadCertificationDetail = async (certId) => {
        try {
            const response = await fetch(`/api/certifications/${certId}`);
            if (!response.ok) throw new Error('Failed to load certification details');
            
            currentCert = await response.json();
            startQuiz();
        } catch (error) {
            console.error('Error fetching certification detail:', error);
            alert('Could not start quiz. Please try again.');
        }
    };

    // --- Render Dashboard ---
    const renderDashboard = () => {
        // Clean out anything (except loader)
        const loader = document.getElementById('dashboard-loading');
        certificationsGrid.innerHTML = '';
        if (loader) certificationsGrid.appendChild(loader);

        if (certifications.length === 0) {
            certificationsGrid.innerHTML += '<p style="text-align: center; grid-column: 1/-1;">No certifications available.</p>';
            return;
        }

        // LEVEL 1: Choose Provider
        if (currentProvider === null) {
            dashboardTitle.textContent = 'Choose Your Provider';
            dashboardSubtitle.textContent = 'Select a cloud or tooling platform to view available certification preparation exams.';

            Object.keys(providers).forEach(providerId => {
                const provider = providers[providerId];
                // Count available exams for this provider
                const count = certifications.filter(c => c.provider === providerId).length;

                const card = document.createElement('div');
                card.className = 'cert-card';
                card.innerHTML = `
                    <div class="cert-icon">${provider.icon}</div>
                    <h2 class="cert-title">${provider.name}</h2>
                    <p class="cert-desc">${provider.desc}</p>
                    <div class="cert-meta">
                        <span class="cert-q-count">${count} Certification${count === 1 ? '' : 's'}</span>
                        <button class="primary-btn view-provider-btn" data-provider="${providerId}" ${count === 0 ? 'disabled' : ''}>View Exams</button>
                    </div>
                `;

                card.querySelector('.view-provider-btn').addEventListener('click', () => {
                    currentProvider = providerId;
                    renderDashboard();
                });

                certificationsGrid.appendChild(card);
            });
        }
        // LEVEL 2: Choose Exam within Provider
        else {
            const providerInfo = providers[currentProvider];
            dashboardTitle.textContent = `${providerInfo.name} Exams`;
            dashboardSubtitle.textContent = `Select an exam to begin practicing.`;

            // Back button
            const backBtn = document.createElement('button');
            backBtn.className = 'text-btn flex-btn';
            backBtn.style.gridColumn = '1 / -1';
            backBtn.style.marginBottom = '20px';
            backBtn.innerHTML = `<span class="btn-arrow">&larr;</span> Back to Providers`;
            backBtn.addEventListener('click', () => {
                currentProvider = null;
                renderDashboard();
            });
            certificationsGrid.appendChild(backBtn);

            const filtered = certifications.filter(c => c.provider === currentProvider);

            if (filtered.length === 0) {
                const emptyMsg = document.createElement('p');
                emptyMsg.style.textAlign = 'center';
                emptyMsg.style.gridColumn = '1 / -1';
                emptyMsg.textContent = 'No exams available under this category yet.';
                certificationsGrid.appendChild(emptyMsg);
                return;
            }

            filtered.forEach(cert => {
                const card = document.createElement('div');
                card.className = 'cert-card';
                card.innerHTML = `
                    <div class="cert-icon">${cert.icon || '📄'}</div>
                    <h2 class="cert-title">${cert.name}</h2>
                    <p class="cert-desc">${cert.description}</p>
                    <div class="cert-meta">
                        <span class="cert-q-count">${cert.questionCount} Questions</span>
                        <button class="primary-btn start-cert-btn" data-id="${cert.id}">Start Practice</button>
                    </div>
                `;

                card.querySelector('.start-cert-btn').addEventListener('click', (e) => {
                    const id = e.target.getAttribute('data-id');
                    loadCertificationDetail(id);
                });

                certificationsGrid.appendChild(card);
            });
        }
    };

    // --- Quiz Practice Loop ---
    const startQuiz = () => {
        currentQuestionIndex = 0;
        score = 0;
        switchView('quiz');
        showQuestion();
    };

    const showQuestion = () => {
        if (!currentCert || !currentCert.questions || currentCert.questions.length === 0) return;
        
        selectedOptionIndex = null;
        submitAnswerBtn.disabled = true;
        submitAnswerBtn.classList.remove('hidden');
        nextQuestionBtn.classList.add('hidden');
        feedbackCard.classList.add('hidden');
        
        const question = currentCert.questions[currentQuestionIndex];
        
        // Progress display
        const total = currentCert.questions.length;
        quizProgressText.textContent = `Question ${currentQuestionIndex + 1} of ${total}`;
        const pct = ((currentQuestionIndex) / total) * 100;
        quizProgressBar.style.width = `${pct}%`;

        // Render question text
        questionText.textContent = question.question;

        // Render options list
        optionsContainer.innerHTML = '';
        question.options.forEach((optionText, idx) => {
            const letter = String.fromCharCode(65 + idx); // A, B, C, D...
            const optionLabel = document.createElement('div');
            optionLabel.className = 'option-label';
            optionLabel.setAttribute('data-index', idx);
            optionLabel.innerHTML = `
                <input type="radio" name="quiz-option" id="opt-${idx}" value="${idx}" class="option-radio">
                <span class="option-letter">${letter}</span>
                <span class="option-text">${escapeHtml(optionText)}</span>
            `;

            // Event listener for selection
            optionLabel.addEventListener('click', () => {
                if (optionLabel.classList.contains('locked')) return;
                
                // Remove selected class from siblings
                const allOptions = optionsContainer.querySelectorAll('.option-label');
                allOptions.forEach(opt => opt.classList.remove('selected'));

                // Set selection
                optionLabel.classList.add('selected');
                const radioInput = optionLabel.querySelector('.option-radio');
                radioInput.checked = true;
                
                selectedOptionIndex = idx;
                submitAnswerBtn.disabled = false;
            });

            optionsContainer.appendChild(optionLabel);
        });
    };

    const submitAnswer = (e) => {
        e.preventDefault();
        if (selectedOptionIndex === null || !currentCert) return;

        const question = currentCert.questions[currentQuestionIndex];
        const isCorrect = selectedOptionIndex === question.correctAnswerIndex;
        
        if (isCorrect) score++;

        // Lock options & color code
        const allOptionLabels = optionsContainer.querySelectorAll('.option-label');
        allOptionLabels.forEach((label, idx) => {
            label.classList.add('locked');
            if (idx === question.correctAnswerIndex) {
                label.classList.add('correct');
            } else if (idx === selectedOptionIndex) {
                label.classList.add('incorrect');
            }
        });

        // Feedback card display
        feedbackCard.className = 'feedback-card ' + (isCorrect ? 'correct-style' : 'incorrect-style');
        feedbackStatusIcon.textContent = isCorrect ? '✓' : '✗';
        feedbackStatusTitle.textContent = isCorrect ? 'Correct!' : 'Incorrect';
        explanationText.textContent = question.explanation;
        feedbackCard.classList.remove('hidden');

        // Toggle action buttons
        submitAnswerBtn.classList.add('hidden');
        nextQuestionBtn.classList.remove('hidden');

        // Scroll down slightly so explanation is in view
        setTimeout(() => {
            feedbackCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 100);
    };

    const handleNextQuestion = () => {
        currentQuestionIndex++;
        if (currentQuestionIndex < currentCert.questions.length) {
            showQuestion();
        } else {
            // Quiz finished - update progress bar to full first
            quizProgressBar.style.width = '100%';
            setTimeout(() => {
                showScorecard();
            }, 300);
        }
    };

    // --- Scorecard Render ---
    const showScorecard = () => {
        if (!currentCert) return;

        scorecardCertName.textContent = currentCert.name;
        
        const total = currentCert.questions.length;
        const scorePct = Math.round((score / total) * 100);
        
        scorePercentage.textContent = `${scorePct}%`;
        scoreFraction.textContent = `${score} / ${total}`;

        const scoreCircle = document.querySelector('.score-circle');
        scoreCircle.className = 'score-circle'; // Reset classes

        const isPassing = scorePct >= 70; // 70% threshold standard
        
        if (isPassing) {
            scorecardBadge.textContent = '🎉';
            scoreCircle.classList.add('pass');
            resultStatusTitle.textContent = 'Congratulations, you passed!';
            resultStatusMessage.textContent = `Excellent job! You answered ${score} out of ${total} questions correctly (${scorePct}%) and met the benchmark logic for certification readiness.`;
        } else {
            scorecardBadge.textContent = '📚';
            scoreCircle.classList.add('fail');
            resultStatusTitle.textContent = 'Keep practicing!';
            resultStatusMessage.textContent = `You scored ${score} out of ${total} (${scorePct}%). We recommend reviewing the detailed explanations and retrying until you achieve at least 70%.`;
        }

        switchView('scorecard');
    };

    // --- Utility helper ---
    const escapeHtml = (text) => {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, function(m) { return map[m]; });
    };

    // --- Action Listeners ---
    quizForm.addEventListener('submit', submitAnswer);
    nextQuestionBtn.addEventListener('click', handleNextQuestion);

    backToDashboardBtn.addEventListener('click', () => {
        if (confirm('Are you sure you want to quit the current practice quiz session? Progress will be lost.')) {
            currentProvider = null; // Reset back to provider selection
            renderDashboard();
            switchView('dashboard');
        }
    });

    retryQuizBtn.addEventListener('click', () => {
        startQuiz();
    });

    returnDashboardBtn.addEventListener('click', () => {
        currentProvider = null; // Reset back to provider selection
        renderDashboard();
        switchView('dashboard');
    });

    headerLogoBtn.addEventListener('click', () => {
        // If in middle of a quiz, ask first
        if (quizView.classList.contains('active')) {
            if (confirm('Are you sure you want to return to dashboard? Current progress will be lost.')) {
                currentProvider = null;
                renderDashboard();
                switchView('dashboard');
            }
        } else {
            currentProvider = null;
            renderDashboard();
            switchView('dashboard');
        }
    });

    // --- Init App ---
    initTheme();
    fetchCertifications();
});
