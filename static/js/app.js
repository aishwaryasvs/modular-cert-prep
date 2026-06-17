document.addEventListener('DOMContentLoaded', () => {
    // --- Application State ---
    let certifications = [];
    let currentCert = null;
    let currentProvider = 'google-cloud'; // Default active provider

    // Active session state (null when not in quiz)
    let activeSession = null;
    
    // Active flashcard state
    let currentFlashcards = [];
    let currentFlashcardIndex = 0;
    let flashcardViewMode = 'checklist'; // 'checklist' or 'study'
    let currentView = 'dashboard';

    // Providers registry
    const providers = {
        'google-cloud': { 
            name: 'Google Cloud', 
            icon: `<svg viewBox="0 0 24 24" width="20" height="20" style="vertical-align: middle;">
                <path d="M12 2L4 6.5 L12 11 L20 6.5 Z" fill="#FBBC05"/>
                <path d="M4 6.5 L4 15.5 L12 20 L12 11 Z" fill="#4285F4"/>
                <path d="M12 11 L12 20 L20 15.5 L20 6.5 Z" fill="#EA4335"/>
                <path d="M12 11L4 6.5" stroke="#34A853" stroke-width="1"/>
            </svg>`, 
            desc: 'Google Cloud Platform professional exam preparation.' 
        },
        'aws': { 
            name: 'AWS', 
            icon: `<svg viewBox="0 0 24 24" width="20" height="20" style="vertical-align: middle;">
                <path d="M4.5 16.5c3.2 2 7.8 2.5 11.2 1.2 2.5-1 4-2.8 4.6-3.8" stroke="#FF9900" stroke-width="2" stroke-linecap="round" fill="none"/>
                <path d="M20.3 13.8l-0.8 2.8m0.8-2.8l-2.8 0.8" stroke="#FF9900" stroke-width="2" stroke-linecap="round" fill="none"/>
                <text x="3" y="11" fill="currentColor" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-weight="800" font-size="9px" letter-spacing="-0.5px">aws</text>
            </svg>`, 
            desc: 'Amazon Web Services cloud computing certifications.' 
        },
        'dbt': { 
            name: 'dbt', 
            icon: `<svg viewBox="0 0 24 24" width="20" height="20" style="vertical-align: middle;">
                <path d="M12 2L3 7v10l9 5 9-5V7l-9-5zm7 14.2l-7 3.9-7-3.9V8.8l7-3.9 7 3.9v7.4z" fill="#FF6B4A"/>
                <polygon points="12,7 7,10 7,14 12,17 17,14 17,10" fill="#FF6B4A" opacity="0.8"/>
            </svg>`, 
            desc: 'dbt Analytics Engineering modeling & engineering tests.' 
        },
        'microsoft': { 
            name: 'Microsoft', 
            icon: `<svg viewBox="0 0 23 23" width="20" height="20" style="vertical-align: middle;">
                <rect x="0" y="0" width="10.5" height="10.5" fill="#F25022"/>
                <rect x="11.5" y="0" width="10.5" height="10.5" fill="#7FBA00"/>
                <rect x="0" y="11.5" width="10.5" height="10.5" fill="#00A4EF"/>
                <rect x="11.5" y="11.5" width="10.5" height="10.5" fill="#FFB900"/>
            </svg>`, 
            desc: 'Microsoft Azure cloud platform technologies.' 
        }
    };


    // --- DOM Elements ---
    // Sidebar
    const appSidebar = document.getElementById('app-sidebar');
    const sidebarProvidersList = document.getElementById('sidebar-providers-list');
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const sidebarCloseBtn = document.getElementById('sidebar-close-btn');
    const sidebarLogoBtn = document.getElementById('sidebar-logo-btn');
    const themeToggleOptions = document.querySelectorAll('.theme-toggle-option');

    // Breadcrumbs & Header
    const headerBreadcrumbs = document.getElementById('header-breadcrumbs');
    const headerStatusArea = document.getElementById('header-status-area');

    // Views
    const dashboardView = document.getElementById('dashboard-view');
    const quizConfigView = document.getElementById('quiz-config-view');
    const quizView = document.getElementById('quiz-view');
    const scorecardView = document.getElementById('scorecard-view');

    // Dashboard
    const certificationsGrid = document.getElementById('certifications-grid');
    const cheatsheetsGrid = document.getElementById('cheatsheets-grid');
    const flashcardsGrid = document.getElementById('flashcards-grid');
    const checklistGrid = document.getElementById('checklist-grid');
    const metricsGrid = document.getElementById('metrics-grid');
    const tabPracticeExams = document.getElementById('tab-practice-exams');
    const tabCheatsheets = document.getElementById('tab-cheatsheets');
    const tabFlashcards = document.getElementById('tab-flashcards');
    const tabChecklist = document.getElementById('tab-checklist');
    const tabMetrics = document.getElementById('tab-metrics');
    const dashboardLoading = document.getElementById('dashboard-loading');

    // Metrics DOM Elements
    const metricTotalAttempts = document.getElementById('metric-total-attempts');
    const metricAvgScore = document.getElementById('metric-avg-score');
    const metricPassRate = document.getElementById('metric-pass-rate');
    const metricTotalQuestions = document.getElementById('metric-total-questions');
    const metricsHistoryBody = document.getElementById('metrics-history-body');
    const dashboardTitle = document.getElementById('dashboard-title');
    const dashboardSubtitle = document.getElementById('dashboard-subtitle');

    // Interactive Flashcards View
    const flashcardView = document.getElementById('flashcard-view');
    const flashcardBackBtn = document.getElementById('flashcard-back-btn');
    const flashcardCardElement = document.getElementById('flashcard-card-element');
    const flashcardFrontTitle = document.getElementById('flashcard-front-title');
    const flashcardBackContent = document.getElementById('flashcard-back-content');
    const flashcardPrevBtn = document.getElementById('flashcard-prev-btn');
    const flashcardNextBtn = document.getElementById('flashcard-next-btn');
    const flashcardProgress = document.getElementById('flashcard-progress');
    const flashcardFrontCategory = document.getElementById('flashcard-front-category');
    const flashcardBackCategory = document.getElementById('flashcard-back-category');

    // Cheatsheet View
    const cheatsheetView = document.getElementById('cheatsheet-view');
    const cheatsheetBackBtn = document.getElementById('cheatsheet-back-btn');
    const cheatsheetTitle = document.getElementById('cheatsheet-title');
    const cheatsheetDesc = document.getElementById('cheatsheet-desc');
    const csSummaryText = document.getElementById('cs-summary-text');
    const csCoreServices = document.getElementById('cs-core-services');
    const csCommands = document.getElementById('cs-commands');
    const csPatterns = document.getElementById('cs-patterns');

    // Exam Guide Checklist View
    const checklistView = document.getElementById('checklist-view');
    const checklistBackBtn = document.getElementById('checklist-back-btn');
    const checklistTitle = document.getElementById('checklist-title');
    const checklistSubtitle = document.getElementById('checklist-subtitle');
    const checklistProgressText = document.getElementById('checklist-progress-text');
    const checklistResetBtn = document.getElementById('checklist-reset-btn');
    const checklistProgressBar = document.getElementById('checklist-progress-bar');
    const checklistContent = document.getElementById('checklist-content');

    // Config View
    const configBackBtn = document.getElementById('config-back-btn');
    const configExamTitle = document.getElementById('config-exam-title');
    const configExamDesc = document.getElementById('config-exam-desc');
    const quizConfigForm = document.getElementById('quiz-config-form');

    // Quiz View
    const quitQuizBtn = document.getElementById('quit-quiz-btn');
    const quizDifficultyBadge = document.getElementById('quiz-difficulty-badge');
    const quizProgressText = document.getElementById('quiz-progress-text');
    const quizProgressBar = document.getElementById('quiz-progress-bar');
    const questionText = document.getElementById('question-text');
    const quizForm = document.getElementById('quiz-form');
    const optionsContainer = document.getElementById('options-container');
    
    // Actions
    const flagContainer = document.getElementById('flag-container');
    const flagCheckbox = document.getElementById('flag-checkbox');
    const prevQuestionBtn = document.getElementById('prev-question-btn');
    const submitAnswerBtn = document.getElementById('submit-answer-btn');
    const nextQuestionBtn = document.getElementById('next-question-btn');
    
    // Simulation Panel
    const quizSidebarPanel = document.getElementById('quiz-sidebar-panel');
    const timerDisplayCard = document.getElementById('timer-display-card');
    const quizTimer = document.getElementById('quiz-timer');
    const questionGridNav = document.getElementById('question-grid-nav');
    const submitExamBtn = document.getElementById('submit-exam-btn');

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
    const reviewQuestionsList = document.getElementById('review-questions-list');
    const retryQuizBtn = document.getElementById('retry-quiz-btn');
    const returnDashboardBtn = document.getElementById('return-dashboard-btn');

    // --- Theme Management ---
    const initTheme = () => {
        const savedTheme = localStorage.getItem('theme') || 'dark';
        document.body.classList.remove('light-theme', 'cyberpunk-theme', 'cobalt-theme');
        if (savedTheme !== 'dark') {
            document.body.classList.add(`${savedTheme}-theme`);
        }
        document.body.setAttribute('data-theme-active', savedTheme);
        
        themeToggleOptions.forEach(opt => {
            if (opt.getAttribute('data-theme') === savedTheme) {
                opt.classList.add('active');
            } else {
                opt.classList.remove('active');
            }
        });
    };

    themeToggleOptions.forEach(opt => {
        opt.addEventListener('click', () => {
            const selectedTheme = opt.getAttribute('data-theme');
            document.body.classList.remove('light-theme', 'cyberpunk-theme', 'cobalt-theme');
            if (selectedTheme !== 'dark') {
                document.body.classList.add(`${selectedTheme}-theme`);
            }
            document.body.setAttribute('data-theme-active', selectedTheme);
            
            themeToggleOptions.forEach(o => o.classList.remove('active'));
            opt.classList.add('active');
            
            localStorage.setItem('theme', selectedTheme);
        });
    });

    // --- Mobile Sidebar Toggle ---
    mobileMenuToggle.addEventListener('click', () => {
        appSidebar.classList.add('open');
    });

    sidebarCloseBtn.addEventListener('click', () => {
        appSidebar.classList.remove('open');
    });

    // Close sidebar on mobile click of logo
    sidebarLogoBtn.addEventListener('click', () => {
        appSidebar.classList.remove('open');
        handleNavigationExit(() => {
            switchView('dashboard');
            renderDashboard();
        });
    });

    // --- View Router ---
    const switchView = (viewName) => {
        currentView = viewName;
        const views = [dashboardView, quizConfigView, quizView, cheatsheetView, flashcardView, scorecardView, checklistView];
        views.forEach(view => {
            view.classList.remove('active');
        });

        // Hide config pane context in header
        if (viewName === 'dashboard') {
            headerBreadcrumbs.textContent = providers[currentProvider] ? providers[currentProvider].name : 'Dashboard';
            headerStatusArea.innerHTML = '';
        }

        setTimeout(() => {
            if (viewName === 'dashboard') dashboardView.classList.add('active');
            if (viewName === 'quiz-config') quizConfigView.classList.add('active');
            if (viewName === 'quiz') quizView.classList.add('active');
            if (viewName === 'cheatsheet') cheatsheetView.classList.add('active');
            if (viewName === 'flashcard') flashcardView.classList.add('active');
            if (viewName === 'checklist') checklistView.classList.add('active');
            if (viewName === 'scorecard') scorecardView.classList.add('active');
        }, 150);
    };

    // Warn if active session exists when clicking nav
    const handleNavigationExit = (callback) => {
        if (activeSession) {
            if (confirm('Are you sure you want to exit your active study/testing session? All current progress will be lost.')) {
                cleanupActiveSession();
                callback();
            }
        } else {
            callback();
        }
    };

    const cleanupActiveSession = () => {
        if (activeSession && activeSession.timerInterval) {
            clearInterval(activeSession.timerInterval);
        }
        activeSession = null;
    };

    // --- Render Sidebar Providers ---
    const renderSidebar = () => {
        sidebarProvidersList.innerHTML = '';
        Object.keys(providers).forEach(providerId => {
            const provider = providers[providerId];
            
            const btn = document.createElement('button');
            btn.className = `nav-item ${providerId === currentProvider ? 'active' : ''}`;
            btn.setAttribute('data-provider', providerId);
            btn.innerHTML = `
                <span class="nav-icon">${provider.icon}</span>
                <span class="nav-label">${provider.name}</span>
            `;

            btn.addEventListener('click', () => {
                handleNavigationExit(() => {
                    currentProvider = providerId;
                    
                    // Set active class visually
                    const allItems = sidebarProvidersList.querySelectorAll('.nav-item');
                    allItems.forEach(i => i.classList.remove('active'));
                    btn.classList.add('active');

                    // Close sidebar on mobile
                    appSidebar.classList.remove('open');

                    switchView('dashboard');
                    renderDashboard();
                });
            });

            sidebarProvidersList.appendChild(btn);
        });
    };

    // --- Fetch API ---
    const fetchCertifications = async () => {
        try {
            dashboardLoading.classList.remove('hidden');
            const response = await fetch('/api/certifications');
            if (!response.ok) throw new Error('Failed to load certifications');
            
            certifications = await response.json();
            renderSidebar();
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
            showQuizConfigScreen();
        } catch (error) {
            console.error('Error fetching certification detail:', error);
            alert('Could not fetch certification settings. Please try again.');
        }
    };

    const loadCheatsheetDetail = async (certId) => {
        try {
            const response = await fetch(`/api/certifications/${certId}`);
            if (!response.ok) throw new Error('Failed to load certification details');
            
            currentCert = await response.json();
            showCheatsheet();
        } catch (error) {
            console.error('Error fetching cheatsheet details:', error);
            alert('Could not fetch cheat sheet details. Please try again.');
        }
    };

    const showCheatsheet = () => {
        if (!currentCert || !currentCert.cheatsheet) return;

        headerBreadcrumbs.textContent = `${providers[currentProvider].name} / ${currentCert.name} / Cheat Sheet`;
        
        cheatsheetTitle.textContent = `${currentCert.name} Cheat Sheet`;
        cheatsheetDesc.textContent = `Essential study guide covering core concepts, CLI commands, and architectural patterns.`;
        
        const cheatsheetSearchInput = document.getElementById('cheatsheet-search-input');
        if (cheatsheetSearchInput) {
            cheatsheetSearchInput.value = '';
        }

        // Summary
        csSummaryText.textContent = currentCert.cheatsheet.summary || "No overview summary provided.";

        // Core Concepts & Services
        csCoreServices.innerHTML = '';
        if (currentCert.cheatsheet.coreConcepts && currentCert.cheatsheet.coreConcepts.length > 0) {
            currentCert.cheatsheet.coreConcepts.forEach(concept => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <strong>${escapeHtml(concept.name)}</strong>
                    <span>${escapeHtml(concept.desc)}</span>
                `;
                csCoreServices.appendChild(li);
            });
        } else {
            csCoreServices.innerHTML = '<li>No core concepts listed.</li>';
        }

        // CLI Commands
        csCommands.innerHTML = '';
        if (currentCert.cheatsheet.commands && currentCert.cheatsheet.commands.length > 0) {
            currentCert.cheatsheet.commands.forEach(cmd => {
                const div = document.createElement('div');
                div.className = 'cmd-item';
                div.innerHTML = `
                    <div class="cmd-code-row">
                        <code class="cmd-code">${escapeHtml(cmd.cmd)}</code>
                        <button class="copy-cmd-btn" title="Copy command">📋</button>
                    </div>
                    <span class="cmd-desc">${escapeHtml(cmd.desc)}</span>
                `;
                
                div.querySelector('.copy-cmd-btn').addEventListener('click', (e) => {
                    navigator.clipboard.writeText(cmd.cmd).then(() => {
                        const btn = e.currentTarget;
                        const originalText = btn.textContent;
                        btn.textContent = '✓';
                        btn.style.color = 'var(--success)';
                        showToastNotification('Command copied to clipboard!');
                        setTimeout(() => {
                            btn.textContent = originalText;
                            btn.style.color = '';
                        }, 2000);
                    });
                });
                
                csCommands.appendChild(div);
            });
        } else {
            csCommands.innerHTML = '<div class="cmd-item"><span class="cmd-desc">No CLI commands configured for this exam.</span></div>';
        }

        // Architectural Patterns
        csPatterns.innerHTML = '';
        if (currentCert.cheatsheet.architecturalPatterns && currentCert.cheatsheet.architecturalPatterns.length > 0) {
            currentCert.cheatsheet.architecturalPatterns.forEach(pattern => {
                const div = document.createElement('div');
                div.className = 'pattern-item';
                div.innerHTML = `
                    <div class="pattern-scenario">${escapeHtml(pattern.scenario)}</div>
                    <div class="pattern-solution">${escapeHtml(pattern.solution)}</div>
                `;
                csPatterns.appendChild(div);
            });
        } else {
            csPatterns.innerHTML = '<div class="pattern-item"><div class="pattern-solution">No design patterns configured for this exam.</div></div>';
        }

        switchView('cheatsheet');
    };

    cheatsheetBackBtn.addEventListener('click', () => {
        switchView('dashboard');
        renderDashboard();
    });

    // --- Interactive Flashcards ---
    const loadStudyFlashcardDetail = async (certId) => {
        try {
            const response = await fetch(`/api/certifications/${certId}`);
            if (!response.ok) throw new Error('Failed to load certification details');
            
            currentCert = await response.json();
            currentFlashcards = currentCert.study_flashcards || [];
            currentFlashcardIndex = 0;
            flashcardViewMode = 'study';
            showFlashcards();
        } catch (error) {
            console.error('Error fetching study flashcards:', error);
            alert('Could not fetch study flashcard details. Please try again.');
        }
    };

    const showFlashcards = () => {
        if (!currentFlashcards || currentFlashcards.length === 0) {
            alert("No flashcards configured for this certification.");
            return;
        }

        headerBreadcrumbs.textContent = `${providers[currentProvider].name} / ${currentCert.name} / Study Flashcards`;
        
        // Update title
        const flashcardTitleHeader = document.getElementById('flashcard-title');
        const flashcardSubtitle = document.getElementById('flashcard-subtitle');
        if (flashcardTitleHeader) {
            flashcardTitleHeader.textContent = `${currentCert.name} Study Flashcards`;
        }
        if (flashcardSubtitle) {
            flashcardSubtitle.textContent = 'Quick-recall Q&A flashcards covering key services, definitions, CLI commands, and exam gotchas.';
        }

        // Reset card flip state
        flashcardCardElement.classList.remove('flipped');
        
        renderActiveFlashcard();
        switchView('flashcard');
    };

    const renderActiveFlashcard = () => {
        const card = currentFlashcards[currentFlashcardIndex];
        const total = currentFlashcards.length;

        // Populate front
        flashcardFrontCategory.textContent = card.category || "Quick Recall";
        flashcardFrontTitle.textContent = card.front;

        // Populate back
        flashcardBackCategory.textContent = (card.category || "Answer") + " — Answer";
        
        // Format the back content - replace newlines with bullet points
        const lines = card.back.split('\n');
        let html = '<ul style="text-align: left; padding-left: 20px; margin: auto 0; width: 100%;">';
        lines.forEach(line => {
            const cleaned = line.trim().replace(/^-\s*/, '');
            if (cleaned) {
                html += `<li style="margin-bottom: 8px; font-size: 0.92rem; color: var(--text-primary);">${escapeHtml(cleaned)}</li>`;
            }
        });
        html += '</ul>';
        flashcardBackContent.innerHTML = html;

        // Update progress
        flashcardProgress.textContent = `Card ${currentFlashcardIndex + 1} of ${total}`;

        // Disable/enable controls
        flashcardPrevBtn.disabled = currentFlashcardIndex === 0;
        flashcardNextBtn.disabled = currentFlashcardIndex === total - 1;
    };

    // --- Exam Guide Checklist ---
    const loadChecklistDetail = async (certId) => {
        try {
            const response = await fetch(`/api/certifications/${certId}`);
            if (!response.ok) throw new Error('Failed to load certification details');
            
            currentCert = await response.json();
            showChecklist();
        } catch (error) {
            console.error('Error fetching checklist:', error);
            alert('Could not fetch checklist details. Please try again.');
        }
    };

    const showChecklist = () => {
        if (!currentCert) return;

        const checklistData = currentCert.flashcards || [];
        if (checklistData.length === 0) {
            alert("No checklist configured for this certification.");
            return;
        }

        headerBreadcrumbs.textContent = `${providers[currentProvider].name} / ${currentCert.name} / Exam Guide Checklist`;
        checklistTitle.textContent = `${currentCert.name} Exam Guide Checklist`;
        checklistSubtitle.textContent = `Evaluate your readiness by marking off key skills as you master them.`;

        // Render checklist content
        renderChecklist(checklistData);
        switchView('checklist');
    };

    const renderChecklist = (checklistData) => {
        checklistContent.innerHTML = '';

        // Load checked items state from localStorage
        const storageKey = `checklist_progress_${currentCert.id}`;
        let checkedStates = JSON.parse(localStorage.getItem(storageKey)) || {};

        let totalItems = 0;

        checklistData.forEach((domain, domainIndex) => {
            const domainCard = document.createElement('div');
            domainCard.className = 'checklist-domain-card';

            const domainTitle = document.createElement('h3');
            domainTitle.className = 'checklist-domain-title';
            domainTitle.textContent = domain.category || `Domain ${domainIndex + 1}`;
            domainCard.appendChild(domainTitle);

            const domainSubtitle = document.createElement('p');
            domainSubtitle.className = 'checklist-domain-subtitle';
            domainSubtitle.textContent = domain.front;
            domainCard.appendChild(domainSubtitle);

            const itemsList = document.createElement('div');
            itemsList.className = 'checklist-items-list';

            // Split the back field by newline to get checklist items
            const lines = domain.back.split('\n');
            lines.forEach((line, lineIndex) => {
                const cleanedLine = line.trim().replace(/^-\s*/, '');
                if (!cleanedLine) return;

                totalItems++;
                const itemKey = `${domainIndex}_${lineIndex}`;
                const isChecked = checkedStates[itemKey] || false;

                const itemLabel = document.createElement('label');
                itemLabel.className = 'checklist-item';
                if (isChecked) itemLabel.classList.add('checked');

                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.checked = isChecked;
                checkbox.dataset.itemKey = itemKey;

                const checkboxCustom = document.createElement('span');
                checkboxCustom.className = 'checklist-checkbox-custom';

                const textSpan = document.createElement('span');
                textSpan.className = 'checklist-item-text';
                textSpan.textContent = cleanedLine;

                itemLabel.appendChild(checkbox);
                itemLabel.appendChild(checkboxCustom);
                itemLabel.appendChild(textSpan);

                // Checkbox state change listener
                checkbox.addEventListener('change', (e) => {
                    const checked = e.target.checked;
                    
                    // Toggle wrapper styling class
                    if (checked) {
                        itemLabel.classList.add('checked');
                    } else {
                        itemLabel.classList.remove('checked');
                    }

                    // Update localStorage
                    checkedStates[itemKey] = checked;
                    localStorage.setItem(storageKey, JSON.stringify(checkedStates));

                    // Recalculate progress
                    updateChecklistProgress(totalItems);
                });

                itemsList.appendChild(itemLabel);
            });

            domainCard.appendChild(itemsList);
            checklistContent.appendChild(domainCard);
        });

        // Initialize progress bar
        updateChecklistProgress(totalItems);

        // Bind reset button
        checklistResetBtn.onclick = () => {
            if (confirm("Are you sure you want to reset all checked items for this exam checklist?")) {
                localStorage.removeItem(storageKey);
                // Re-render
                renderChecklist(checklistData);
            }
        };
    };

    const updateChecklistProgress = (totalItems) => {
        if (totalItems === 0) return;

        const storageKey = `checklist_progress_${currentCert.id}`;
        const checkedStates = JSON.parse(localStorage.getItem(storageKey)) || {};
        
        let checkedCount = 0;
        // Count how many keys in checkedStates are true
        Object.keys(checkedStates).forEach(key => {
            if (checkedStates[key]) checkedCount++;
        });

        // Cap checkedCount to totalItems to prevent out-of-sync discrepancies
        checkedCount = Math.min(checkedCount, totalItems);

        const percentage = Math.round((checkedCount / totalItems) * 100);
        checklistProgressBar.style.width = `${percentage}%`;
        checklistProgressText.textContent = `${percentage}% Complete (${checkedCount} of ${totalItems} tasks)`;
    };

    // Card Flip trigger
    flashcardCardElement.addEventListener('click', () => {
        flashcardCardElement.classList.toggle('flipped');
    });

    flashcardPrevBtn.addEventListener('click', (e) => {
        e.stopPropagation(); // prevent flipping the card when clicking controls
        if (currentFlashcardIndex > 0) {
            flashcardCardElement.classList.remove('flipped');
            // Wait briefly for flip transition to finish before changing content
            setTimeout(() => {
                currentFlashcardIndex--;
                renderActiveFlashcard();
            }, 150);
        }
    });

    flashcardNextBtn.addEventListener('click', (e) => {
        e.stopPropagation(); // prevent flipping the card when clicking controls
        if (currentFlashcardIndex < currentFlashcards.length - 1) {
            flashcardCardElement.classList.remove('flipped');
            // Wait briefly for flip transition to finish before changing content
            setTimeout(() => {
                currentFlashcardIndex++;
                renderActiveFlashcard();
            }, 150);
        }
    });

    flashcardBackBtn.addEventListener('click', () => {
        switchView('dashboard');
        renderDashboard();
    });

    checklistBackBtn.addEventListener('click', () => {
        switchView('dashboard');
        renderDashboard();
    });

    // Tab switching handlers
    const allTabBtns = [tabPracticeExams, tabCheatsheets, tabFlashcards, tabChecklist, tabMetrics];
    const allTabGrids = [certificationsGrid, cheatsheetsGrid, flashcardsGrid, checklistGrid, metricsGrid];

    const activateTab = (activeBtn, activeGrid) => {
        allTabBtns.forEach(btn => btn.classList.remove('active'));
        allTabGrids.forEach(grid => grid.classList.add('hidden'));
        activeBtn.classList.add('active');
        activeGrid.classList.remove('hidden');
    };

    tabPracticeExams.addEventListener('click', () => activateTab(tabPracticeExams, certificationsGrid));
    tabCheatsheets.addEventListener('click', () => activateTab(tabCheatsheets, cheatsheetsGrid));
    tabFlashcards.addEventListener('click', () => activateTab(tabFlashcards, flashcardsGrid));
    tabChecklist.addEventListener('click', () => activateTab(tabChecklist, checklistGrid));
    tabMetrics.addEventListener('click', () => {
        activateTab(tabMetrics, metricsGrid);
        fetchAndRenderMetrics();
    });

    const fetchAndRenderMetrics = () => {
        metricsHistoryBody.innerHTML = `<tr><td colspan="6" style="text-align: center; padding: 20px;"><div class="spinner" style="margin: 0 auto;"></div></td></tr>`;
        
        fetch('/api/metrics')
            .then(res => {
                if (!res.ok) throw new Error('Failed to fetch metrics');
                return res.json();
            })
            .then(data => {
                metricTotalAttempts.textContent = data.total_attempts;
                metricAvgScore.textContent = `${data.avg_score}%`;
                metricPassRate.textContent = `${data.simulation_pass_rate}%`;
                metricTotalQuestions.textContent = data.total_questions_answered;

                metricsHistoryBody.innerHTML = '';
                if (data.recent_attempts.length === 0) {
                    metricsHistoryBody.innerHTML = `
                        <tr>
                            <td colspan="6" style="text-align: center; color: var(--text-secondary); padding: 20px;">
                                No quiz attempts logged yet. Start studying to see your stats!
                            </td>
                        </tr>
                    `;
                    return;
                }

                data.recent_attempts.forEach(attempt => {
                    const statusClass = attempt.passed ? 'correct' : 'incorrect';
                    const statusText = attempt.passed ? 'PASS' : 'FAIL';
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <td><strong>${escapeHtml(attempt.certification_name)}</strong> <span style="font-size: 0.75rem; color: var(--text-secondary); opacity: 0.8;">(${attempt.provider.toUpperCase()})</span></td>
                        <td style="text-transform: capitalize;">${escapeHtml(attempt.mode)}</td>
                        <td style="text-transform: capitalize;">${escapeHtml(attempt.difficulty)}</td>
                        <td>${attempt.score}% (${attempt.correct_questions}/${attempt.total_questions})</td>
                        <td><span class="review-badge ${statusClass}" style="display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: bold;">${statusText}</span></td>
                        <td style="white-space: nowrap; font-size: 0.82rem; color: var(--text-secondary);">${escapeHtml(attempt.timestamp)}</td>
                    `;
                    metricsHistoryBody.appendChild(tr);
                });
            })
            .catch(err => {
                console.error(err);
                metricsHistoryBody.innerHTML = `
                    <tr>
                        <td colspan="6" style="text-align: center; color: var(--error); padding: 20px;">
                            Error loading performance metrics. Please try again.
                        </td>
                    </tr>
                `;
            });
    };

    // --- Render Dashboard (Exams under selected provider) ---
    const renderDashboard = () => {
        // Reset tab state to default (Practice Exams active)
        activateTab(tabPracticeExams, certificationsGrid);

        certificationsGrid.innerHTML = '';
        cheatsheetsGrid.innerHTML = '';
        flashcardsGrid.innerHTML = '';
        checklistGrid.innerHTML = '';
        headerBreadcrumbs.textContent = providers[currentProvider] ? providers[currentProvider].name : 'Dashboard';

        const filtered = certifications.filter(c => c.provider === currentProvider);

        if (filtered.length === 0) {
            certificationsGrid.innerHTML = '<p style="text-align: center; grid-column: 1/-1; padding: 40px 0; color: var(--text-secondary);">No certifications available under this provider yet.</p>';
            cheatsheetsGrid.innerHTML = '<p style="text-align: center; grid-column: 1/-1; padding: 40px 0; color: var(--text-secondary);">No study cheat sheets available under this provider yet.</p>';
            flashcardsGrid.innerHTML = '<p style="text-align: center; grid-column: 1/-1; padding: 40px 0; color: var(--text-secondary);">No flashcards available under this provider yet.</p>';
            checklistGrid.innerHTML = '<p style="text-align: center; grid-column: 1/-1; padding: 40px 0; color: var(--text-secondary);">No exam guide checklists available under this provider yet.</p>';
            return;
        }

        dashboardTitle.textContent = `${providers[currentProvider].name} Certifications`;
        dashboardSubtitle.textContent = `Select an option below to study cheat sheets, access resources, or start interactive practice test sessions.`;

        filtered.forEach(cert => {
            // 1. Render Practice Exam Card
            const practiceCard = document.createElement('div');
            practiceCard.className = 'cert-card';
            practiceCard.innerHTML = `
                <div class="cert-icon">${cert.icon || '📄'}</div>
                <h2 class="cert-title">${cert.name}</h2>
                <p class="cert-desc">${cert.description}</p>
                <div class="cert-meta">
                    <span class="cert-q-count">${cert.questionCount} Questions Available</span>
                    <button class="primary-btn start-cert-btn" data-id="${cert.id}">Start Session</button>
                </div>
            `;
            
            practiceCard.querySelector('.start-cert-btn').addEventListener('click', (e) => {
                const id = e.target.getAttribute('data-id');
                loadCertificationDetail(id);
            });

            certificationsGrid.appendChild(practiceCard);

            // 2. Render Cheatsheet Card
            const csCard = document.createElement('div');
            csCard.className = 'cert-card';
            csCard.innerHTML = `
                <div class="cert-icon">${cert.icon || '📄'}</div>
                <h2 class="cert-title">${cert.name} Guide</h2>
                <p class="cert-desc">Core concepts, common CLI command structures, and design solutions for the ${cert.name} exam.</p>
                <div class="cert-meta">
                    <span class="cert-q-count">Study Cheat Sheet</span>
                    <button class="primary-btn view-cs-btn" data-id="${cert.id}">View Cheat Sheet</button>
                </div>
            `;
            
            csCard.querySelector('.view-cs-btn').addEventListener('click', (e) => {
                const id = e.target.getAttribute('data-id');
                loadCheatsheetDetail(id);
            });

            cheatsheetsGrid.appendChild(csCard);

            // 3. Render Study Flashcard Card (Q&A quick-recall style)
            const fcCard = document.createElement('div');
            fcCard.className = 'cert-card';
            fcCard.innerHTML = `
                <div class="cert-icon">${cert.icon || '📄'}</div>
                <h2 class="cert-title">${cert.name} Flashcards</h2>
                <p class="cert-desc">Quick-recall Q&A flashcards covering key services, definitions, CLI commands, and exam gotchas.</p>
                <div class="cert-meta">
                    <span class="cert-q-count">${cert.studyFlashcardCount || 0} Flashcards</span>
                    <button class="primary-btn view-fc-btn" data-id="${cert.id}">Study Flashcards</button>
                </div>
            `;
            
            fcCard.querySelector('.view-fc-btn').addEventListener('click', (e) => {
                const id = e.target.getAttribute('data-id');
                loadStudyFlashcardDetail(id);
            });

            flashcardsGrid.appendChild(fcCard);

            // 4. Render Exam Guide Checklist Card (domain-based official exam guide)
            const clCard = document.createElement('div');
            clCard.className = 'cert-card';
            clCard.innerHTML = `
                <div class="cert-icon">${cert.icon || '📄'}</div>
                <h2 class="cert-title">${cert.name} Checklist</h2>
                <p class="cert-desc">Official exam guide domains and verified skills checklist to evaluate your readiness.</p>
                <div class="cert-meta">
                    <span class="cert-q-count">Exam Guide Checklist</span>
                    <button class="primary-btn view-cl-btn" data-id="${cert.id}">View Checklist</button>
                </div>
            `;
            
            clCard.querySelector('.view-cl-btn').addEventListener('click', (e) => {
                const id = e.target.getAttribute('data-id');
                loadChecklistDetail(id);
            });

            checklistGrid.appendChild(clCard);
        });
    };

    // --- Show Study Config Screen ---
    const showQuizConfigScreen = () => {
        if (!currentCert) return;

        headerBreadcrumbs.textContent = `${providers[currentProvider].name} / ${currentCert.name}`;
        configExamTitle.textContent = `${currentCert.name} - Setup`;
        configExamDesc.textContent = `Choose your study mode and difficulty. Total questions in database: ${currentCert.questions.length}.`;

        // Update radio selected indicators
        const radioCards = quizConfigForm.querySelectorAll('.radio-card');
        radioCards.forEach(card => {
            const input = card.querySelector('input');
            
            // Set initial selected styling
            if (input.checked) {
                card.classList.add('selected');
            } else {
                card.classList.remove('selected');
            }

            // Click listener
            card.addEventListener('click', () => {
                const groupName = input.name;
                const siblings = quizConfigForm.querySelectorAll(`.radio-card:has(input[name="${groupName}"])`);
                siblings.forEach(s => s.classList.remove('selected'));
                card.classList.add('selected');
                input.checked = true;
            });
        });

        switchView('quiz-config');
    };

    configBackBtn.addEventListener('click', () => {
        switchView('dashboard');
        renderDashboard();
    });

    // --- Launch Session ---
    quizConfigForm.addEventListener('submit', (e) => {
        e.preventDefault();
        if (!currentCert) return;

        const formData = new FormData(quizConfigForm);
        const difficulty = formData.get('difficulty'); // 'all', 'easy', 'medium', 'hard'
        const mode = formData.get('mode'); // 'practice', 'exam'

        // Filter questions by difficulty
        let pool = [];
        if (difficulty === 'all') {
            pool = [...currentCert.questions];
        } else {
            pool = currentCert.questions.filter(q => q.difficulty === difficulty);
        }

        if (pool.length === 0) {
            alert(`No questions found matching the "${difficulty.toUpperCase()}" difficulty level. Please choose another configuration.`);
            return;
        }

        // Initialize session parameters
        activeSession = {
            mode: mode,
            difficulty: difficulty,
            questions: pool,
            currentQuestionIndex: 0,
            answers: new Array(pool.length).fill(null),
            flagged: new Array(pool.length).fill(false),
            score: 0,
            timeRemaining: 20 * 60, // 20 minutes default for Exam mode
            timerInterval: null,
            timeElapsed: 0
        };

        // If Exam Simulation, Shuffe & Limit to 20 questions
        if (mode === 'exam') {
            activeSession.questions = shuffleArray(activeSession.questions).slice(0, 20);
            // Re-allocate arrays based on slice
            activeSession.answers = new Array(activeSession.questions.length).fill(null);
            activeSession.flagged = new Array(activeSession.questions.length).fill(false);
            
            // Start simulation timer
            startTimer();
        }

        // Configure UI Mode displays
        if (mode === 'exam') {
            quizSidebarPanel.classList.remove('hidden');
            flagContainer.classList.remove('hidden');
            prevQuestionBtn.classList.remove('hidden');
            submitAnswerBtn.classList.add('hidden'); // No direct submit button per question
            nextQuestionBtn.classList.remove('hidden'); // Navigate freely
            
            // Build navigation grid
            buildQuestionNavigationGrid();
        } else {
            quizSidebarPanel.classList.add('hidden');
            flagContainer.classList.add('hidden');
            prevQuestionBtn.classList.add('hidden');
            submitAnswerBtn.classList.remove('hidden');
            nextQuestionBtn.classList.add('hidden');
        }

        switchView('quiz');
        showQuestion();
    });

    // Shuffler
    const shuffleArray = (array) => {
        const arr = [...array];
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(randomSeed() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    };

    // Deterministic random seed fallback
    let seed = 42;
    const randomSeed = () => {
        let x = Math.sin(seed++) * 10000;
        return x - Math.floor(x);
    };

    // --- Timer (Simulation Mode) ---
    const startTimer = () => {
        if (!activeSession) return;
        
        timerDisplayCard.classList.remove('low-time');
        updateTimerDisplay();

        activeSession.timerInterval = setInterval(() => {
            if (!activeSession) return;

            activeSession.timeRemaining--;
            activeSession.timeElapsed++;
            
            updateTimerDisplay();

            if (activeSession.timeRemaining <= 120) { // Under 2 mins left
                timerDisplayCard.classList.add('low-time');
            }

            if (activeSession.timeRemaining <= 0) {
                clearInterval(activeSession.timerInterval);
                alert("Exam Time Expired! Your exam will be automatically submitted.");
                submitExam();
            }
        }, 1000);
    };

    const updateTimerDisplay = () => {
        if (!activeSession) return;
        const mins = Math.floor(activeSession.timeRemaining / 60);
        const secs = activeSession.timeRemaining % 60;
        quizTimer.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        headerStatusArea.innerHTML = `<span class="timer-badge" style="color: var(--accent-primary); font-weight: 700;">⏱️ ${quizTimer.textContent}</span>`;
    };

    // --- Build Question Navigation Grid (Simulation Mode) ---
    const buildQuestionNavigationGrid = () => {
        if (!activeSession) return;

        questionGridNav.innerHTML = '';
        activeSession.questions.forEach((_, idx) => {
            const btn = document.createElement('button');
            btn.className = 'grid-nav-btn';
            btn.textContent = (idx + 1).toString();
            btn.setAttribute('data-index', idx);

            btn.addEventListener('click', () => {
                saveSelectedAnswerInState(); // Save current work
                activeSession.currentQuestionIndex = idx;
                showQuestion();
            });

            questionGridNav.appendChild(btn);
        });
        updateQuestionNavigationGridState();
    };

    const updateQuestionNavigationGridState = () => {
        if (!activeSession || activeSession.mode !== 'exam') return;

        let answeredCount = 0;
        let flaggedCount = 0;
        let unansweredCount = 0;

        const buttons = questionGridNav.querySelectorAll('.grid-nav-btn');
        buttons.forEach((btn, idx) => {
            btn.className = 'grid-nav-btn';

            if (idx === activeSession.currentQuestionIndex) {
                btn.classList.add('current');
            }

            if (activeSession.flagged[idx]) {
                btn.classList.add('flagged');
                flaggedCount++;
            }

            if (activeSession.answers[idx] !== null) {
                btn.classList.add('answered');
                answeredCount++;
            } else {
                unansweredCount++;
            }
        });

        const summaryAnswered = document.getElementById('summary-answered');
        const summaryFlagged = document.getElementById('summary-flagged');
        const summaryUnanswered = document.getElementById('summary-unanswered');
        if (summaryAnswered) summaryAnswered.textContent = `${answeredCount} Answered`;
        if (summaryFlagged) summaryFlagged.textContent = `${flaggedCount} Flagged`;
        if (summaryUnanswered) summaryUnanswered.textContent = `${unansweredCount} Unanswered`;
    };

    // --- Render Question ---
    const showQuestion = () => {
        if (!activeSession) return;

        const idx = activeSession.currentQuestionIndex;
        const question = activeSession.questions[idx];
        const total = activeSession.questions.length;

        // Header context
        quizDifficultyBadge.className = `badge ${question.difficulty}`;
        quizDifficultyBadge.textContent = question.difficulty;
        quizProgressText.textContent = `Question ${idx + 1} of ${total}`;
        
        // Progress Bar
        const pct = (idx / total) * 100;
        quizProgressBar.style.width = `${pct}%`;

        // Question text
        questionText.textContent = question.question;

        // Clear feedback card
        feedbackCard.classList.add('hidden');

        // Flag checkbox configuration (Simulation mode)
        if (activeSession.mode === 'exam') {
            flagCheckbox.checked = activeSession.flagged[idx];
        }

        // Render options list
        optionsContainer.innerHTML = '';
        question.options.forEach((optionText, optIdx) => {
            const letter = String.fromCharCode(65 + optIdx);
            const label = document.createElement('label');
            label.className = 'option-label';
            label.setAttribute('data-index', optIdx);
            label.innerHTML = `
                <input type="radio" name="quiz-option" id="opt-${optIdx}" value="${optIdx}" class="option-radio">
                <span class="option-letter">${letter}</span>
                <span class="option-text">${escapeHtml(optionText)}</span>
            `;

            // Restore selection if already answered
            const savedAns = activeSession.answers[idx];
            if (savedAns === optIdx) {
                label.classList.add('selected');
                label.querySelector('input').checked = true;
            }

            // Click listener
            label.addEventListener('click', (e) => {
                if (label.classList.contains('locked')) return;

                // Toggle selects
                const siblings = optionsContainer.querySelectorAll('.option-label');
                siblings.forEach(s => s.classList.remove('selected'));
                label.classList.add('selected');
                label.querySelector('input').checked = true;

                if (activeSession.mode === 'practice') {
                    submitAnswerBtn.disabled = false;
                } else {
                    // Simulation Mode: save immediately
                    activeSession.answers[idx] = optIdx;
                    updateQuestionNavigationGridState();
                }
            });

            optionsContainer.appendChild(label);
        });

        // Toggle action buttons layout
        if (activeSession.mode === 'practice') {
            const answered = activeSession.answers[idx] !== null;
            if (answered) {
                // Lock option buttons and reveal feedback
                lockPracticeQuestionAndReveal(idx);
            } else {
                submitAnswerBtn.disabled = true;
                submitAnswerBtn.classList.remove('hidden');
                nextQuestionBtn.classList.add('hidden');
            }
        } else {
            // Simulation Mode: Previous & Next navigation controls
            prevQuestionBtn.disabled = idx === 0;
            
            if (idx === total - 1) {
                nextQuestionBtn.textContent = 'Finish';
                nextQuestionBtn.disabled = true; // Disable Next, user must click submit exam
            } else {
                nextQuestionBtn.textContent = 'Next ➔';
                nextQuestionBtn.disabled = false;
            }
        }
    };

    // Save answer when navigating away (helper)
    const saveSelectedAnswerInState = () => {
        if (!activeSession) return;
        const selected = optionsContainer.querySelector('.option-label.selected');
        const idx = activeSession.currentQuestionIndex;
        if (selected) {
            activeSession.answers[idx] = parseInt(selected.getAttribute('data-index'));
        }
    };

    // --- Practice Mode Submit Answer ---
    quizForm.addEventListener('submit', (e) => {
        e.preventDefault();
        if (!activeSession || activeSession.mode !== 'practice') return;

        const idx = activeSession.currentQuestionIndex;
        const selected = optionsContainer.querySelector('.option-label.selected');
        if (!selected) return;

        const optIdx = parseInt(selected.getAttribute('data-index'));
        activeSession.answers[idx] = optIdx; // Save choice

        lockPracticeQuestionAndReveal(idx);
    });

    const lockPracticeQuestionAndReveal = (idx) => {
        const question = activeSession.questions[idx];
        const userAns = activeSession.answers[idx];
        const isCorrect = userAns === question.correctAnswerIndex;

        // Lock select controls
        const optionLabels = optionsContainer.querySelectorAll('.option-label');
        optionLabels.forEach((label, oIdx) => {
            label.classList.add('locked');
            if (oIdx === question.correctAnswerIndex) {
                label.classList.add('correct');
            } else if (oIdx === userAns) {
                label.classList.add('incorrect');
            }
        });

        // Feedback layout
        feedbackCard.className = 'feedback-card ' + (isCorrect ? 'correct-style' : 'incorrect-style');
        feedbackStatusIcon.textContent = isCorrect ? '✓' : '✗';
        feedbackStatusTitle.textContent = isCorrect ? 'Correct!' : 'Incorrect';
        explanationText.textContent = question.explanation;
        feedbackCard.classList.remove('hidden');

        // Toggle buttons
        submitAnswerBtn.classList.add('hidden');
        nextQuestionBtn.classList.remove('hidden');

        // Scroll explanation into view
        setTimeout(() => {
            feedbackCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 100);
    };

    // --- Navigation click listeners ---
    prevQuestionBtn.addEventListener('click', () => {
        if (!activeSession) return;
        saveSelectedAnswerInState();
        activeSession.currentQuestionIndex--;
        showQuestion();
        updateQuestionNavigationGridState();
    });

    nextQuestionBtn.addEventListener('click', () => {
        if (!activeSession) return;

        if (activeSession.mode === 'practice') {
            const idx = activeSession.currentQuestionIndex;
            if (idx === activeSession.questions.length - 1) {
                showScorecard();
            } else {
                activeSession.currentQuestionIndex++;
                showQuestion();
            }
        } else {
            // Simulation Mode
            saveSelectedAnswerInState();
            activeSession.currentQuestionIndex++;
            showQuestion();
            updateQuestionNavigationGridState();
        }
    });

    // Flag checkbox listener
    flagCheckbox.addEventListener('change', () => {
        if (!activeSession || activeSession.mode !== 'exam') return;
        const idx = activeSession.currentQuestionIndex;
        activeSession.flagged[idx] = flagCheckbox.checked;
        updateQuestionNavigationGridState();
    });

    // --- Submit Entire Exam (Simulation mode) ---
    submitExamBtn.addEventListener('click', () => {
        if (!activeSession) return;

        const unansweredCount = activeSession.answers.filter(ans => ans === null).length;
        let warningText = 'Are you sure you want to finish and submit your exam simulation?';
        if (unansweredCount > 0) {
            warningText = `You have ${unansweredCount} unanswered question(s) left. Are you sure you want to finish and submit your exam now?`;
        }

        showConfirmModal('Submit Simulation?', warningText, () => {
            submitExam();
        });
    });

    const submitExam = () => {
        if (!activeSession) return;

        // Stop timer
        if (activeSession.timerInterval) {
            clearInterval(activeSession.timerInterval);
        }

        // Calculate score
        let correctCount = 0;
        activeSession.questions.forEach((q, idx) => {
            if (activeSession.answers[idx] === q.correctAnswerIndex) {
                correctCount++;
            }
        });
        activeSession.score = correctCount;

        showScorecard();
    };

    // --- Scorecard Render ---
    const showScorecard = () => {
        if (!activeSession || !currentCert) return;

        scorecardCertName.textContent = currentCert.name;
        
        const total = activeSession.questions.length;
        
        // Calculate score
        let correctCount = 0;
        activeSession.questions.forEach((q, idx) => {
            if (activeSession.answers[idx] === q.correctAnswerIndex) {
                correctCount++;
            }
        });
        
        const scorePct = Math.round((correctCount / total) * 100);
        scorePercentage.textContent = `${scorePct}%`;
        scoreFraction.textContent = `${correctCount} / ${total}`;

        // Log quiz attempt to backend database
        fetch('/api/attempts', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                certification_id: currentCert.id,
                score: scorePct,
                total_questions: total,
                correct_questions: correctCount,
                mode: activeSession.mode === 'exam' ? 'simulation' : 'practice',
                difficulty: activeSession.difficulty
            })
        }).catch(err => console.error('Error logging quiz attempt:', err));

        const scoreRingBar = document.getElementById('score-ring-bar');
        if (scoreRingBar) {
            const offset = 440 - (440 * scorePct) / 100;
            scoreRingBar.style.strokeDashoffset = offset;
            
            const isPassing = scorePct >= 70;
            if (isPassing) {
                scoreRingBar.style.stroke = 'var(--success)';
            } else {
                scoreRingBar.style.stroke = 'var(--error)';
            }
        }

        const isPassing = scorePct >= 70; // 70% threshold standard
        
        if (isPassing) {
            scorecardBadge.textContent = '🎉';
            resultStatusTitle.textContent = 'Congratulations, you passed!';
            resultStatusMessage.textContent = `Excellent job! You answered ${correctCount} out of ${total} questions correctly (${scorePct}%) and met the benchmark logic for certification readiness.`;
        } else {
            scorecardBadge.textContent = '📚';
            resultStatusTitle.textContent = 'Keep practicing!';
            resultStatusMessage.textContent = `You scored ${correctCount} out of ${total} (${scorePct}%). We recommend reviewing the detailed explanations below and retrying until you achieve at least 70%.`;
        }

        const allFilterBtn = document.querySelector('.review-filters [data-filter="all"]');
        if (allFilterBtn) {
            const filterButtons = document.querySelectorAll('.review-filters .filter-btn');
            filterButtons.forEach(b => b.classList.remove('active'));
            allFilterBtn.classList.add('active');
        }

        // Render detailed review accordions
        renderReviewQuestions();

        switchView('scorecard');
    };

    const renderReviewQuestions = () => {
        if (!activeSession) return;

        reviewQuestionsList.innerHTML = '';
        activeSession.questions.forEach((question, idx) => {
            const userAnsIdx = activeSession.answers[idx];
            const isCorrect = userAnsIdx === question.correctAnswerIndex;
            const statusText = userAnsIdx === null ? 'Unanswered' : (isCorrect ? 'Correct' : 'Incorrect');
            const statusClass = userAnsIdx === null ? 'incorrect' : (isCorrect ? 'correct' : 'incorrect'); // treating unanswered as incorrect style

            const item = document.createElement('div');
            item.className = 'review-item';
            item.setAttribute('data-correct', isCorrect ? 'true' : 'false');
            item.setAttribute('data-flagged', activeSession.flagged[idx] ? 'true' : 'false');
            item.innerHTML = `
                <div class="review-header-toggle">
                    <span class="review-q-summary">
                        <span class="review-badge ${statusClass}">${statusText}</span>
                        <span>Q${idx + 1}: ${escapeHtml(question.question)}</span>
                    </span>
                    <span class="toggle-arrow">▼</span>
                </div>
                <div class="review-body-wrapper">
                    <div class="review-body">
                        <p class="review-q-text">${escapeHtml(question.question)}</p>
                        <div class="options-list">
                            <!-- Filled dynamically below -->
                        </div>
                        <div class="feedback-card ${isCorrect ? 'correct-style' : 'incorrect-style'}">
                            <div class="explanation-content" style="margin: 0;">
                                <h4>Explanation</h4>
                                <p>${escapeHtml(question.explanation)}</p>
                            </div>
                        </div>
                    </div>
                </div>
            `;

            // Populate options inside review body
            const optsContainer = item.querySelector('.options-list');
            question.options.forEach((opt, oIdx) => {
                const optLabel = document.createElement('div');
                optLabel.className = 'review-option';
                
                // Styling correct, user incorrect, correct etc.
                let stateClass = '';
                if (oIdx === question.correctAnswerIndex) {
                    stateClass = 'correct'; // highlight true correct answer
                } else if (oIdx === userAnsIdx && !isCorrect) {
                    stateClass = 'incorrect'; // highlight incorrect user choice
                }

                optLabel.className = `review-option-card ${stateClass}`;
                optLabel.innerHTML = `
                    <span class="option-marker">${String.fromCharCode(65 + oIdx)}</span>
                    <span class="option-text">${escapeHtml(opt)}</span>
                `;
                optsContainer.appendChild(optLabel);
            });

            // Toggle Open/Close accordion
            item.querySelector('.review-header-toggle').addEventListener('click', () => {
                item.classList.toggle('open');
            });

            reviewQuestionsList.appendChild(item);
        });
    };

    // --- Action Listeners for exiting/retrying quiz ---
    quitQuizBtn.addEventListener('click', () => {
        handleNavigationExit(() => {
            switchView('dashboard');
            renderDashboard();
        });
    });

    retryQuizBtn.addEventListener('click', () => {
        cleanupActiveSession();
        showQuizConfigScreen();
    });

    returnDashboardBtn.addEventListener('click', () => {
        cleanupActiveSession();
        switchView('dashboard');
        renderDashboard();
    });

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

    // --- Glassmorphic Confirmation Modal Helper ---
    const showConfirmModal = (title, text, onOk) => {
        const modal = document.getElementById('confirm-modal');
        const modalTitle = document.getElementById('confirm-modal-title');
        const modalText = document.getElementById('confirm-modal-text');
        const btnCancel = document.getElementById('confirm-modal-cancel');
        const btnOk = document.getElementById('confirm-modal-ok');

        modalTitle.textContent = title;
        modalText.textContent = text;
        modal.classList.remove('hidden');

        // Clone buttons to clear existing event listeners
        const newBtnCancel = btnCancel.cloneNode(true);
        const newBtnOk = btnOk.cloneNode(true);
        btnCancel.parentNode.replaceChild(newBtnCancel, btnCancel);
        btnOk.parentNode.replaceChild(newBtnOk, btnOk);

        newBtnCancel.addEventListener('click', () => {
            modal.classList.add('hidden');
        });

        newBtnOk.addEventListener('click', () => {
            modal.classList.add('hidden');
            onOk();
        });
    };

    // --- Scorecard Question Filters ---
    const applyReviewFilter = (filterType) => {
        const items = reviewQuestionsList.querySelectorAll('.review-item');
        items.forEach(item => {
            const isCorrect = item.getAttribute('data-correct') === 'true';
            const isFlagged = item.getAttribute('data-flagged') === 'true';

            if (filterType === 'all') {
                item.style.display = '';
            } else if (filterType === 'incorrect') {
                item.style.display = !isCorrect ? '' : 'none';
            } else if (filterType === 'flagged') {
                item.style.display = isFlagged ? '' : 'none';
            }
        });
    };

    const filterButtons = document.querySelectorAll('.review-filters .filter-btn');
    filterButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            filterButtons.forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            const filter = e.target.getAttribute('data-filter');
            applyReviewFilter(filter);
        });
    });

    // --- Cheatsheet Local Search Filter ---
    const cheatsheetSearchInput = document.getElementById('cheatsheet-search-input');
    if (cheatsheetSearchInput) {
        cheatsheetSearchInput.addEventListener('input', () => {
            const query = cheatsheetSearchInput.value.toLowerCase().trim();
            
            // Concepts list
            csCoreServices.querySelectorAll('li').forEach(item => {
                item.style.display = item.textContent.toLowerCase().includes(query) ? '' : 'none';
            });

            // Commands list
            csCommands.querySelectorAll('.cmd-item').forEach(item => {
                item.style.display = item.textContent.toLowerCase().includes(query) ? '' : 'none';
            });

            // Scenarios list
            csPatterns.querySelectorAll('.pattern-item').forEach(item => {
                item.style.display = item.textContent.toLowerCase().includes(query) ? '' : 'none';
            });
        });
    }

    // --- Keyboard Hotkeys & Navigation ---
    document.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
            return;
        }

        if (currentView === 'flashcard') {
            if (e.key === ' ' || e.code === 'Space') {
                e.preventDefault();
                flashcardCardElement.click();
            } else if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') {
                flashcardNextBtn.click();
            } else if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') {
                flashcardPrevBtn.click();
            }
        } else if (currentView === 'quiz') {
            if (!activeSession) return;

            if (e.key >= '1' && e.key <= '4') {
                const index = parseInt(e.key) - 1;
                const options = optionsContainer.querySelectorAll('input[type="radio"], input[type="checkbox"]');
                if (options && options[index]) {
                    options[index].click();
                }
            } else if (e.key.toLowerCase() === 'f') {
                const flagCheckbox = document.getElementById('flag-checkbox');
                const flagContainer = document.getElementById('flag-container');
                if (flagCheckbox && flagContainer && !flagContainer.classList.contains('hidden')) {
                    flagCheckbox.click();
                }
            } else if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') {
                const nextBtn = document.getElementById('next-question-btn');
                if (nextBtn && !nextBtn.classList.contains('hidden')) {
                    nextBtn.click();
                }
            } else if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') {
                const prevBtn = document.getElementById('prev-question-btn');
                if (prevBtn && !prevBtn.classList.contains('hidden')) {
                    prevBtn.click();
                }
            } else if (e.key === 'Enter') {
                const submitBtn = document.getElementById('submit-answer-btn');
                const nextBtn = document.getElementById('next-question-btn');
                if (submitBtn && !submitBtn.disabled && !submitBtn.classList.contains('hidden')) {
                    e.preventDefault();
                    submitBtn.click();
                } else if (nextBtn && !nextBtn.classList.contains('hidden')) {
                    e.preventDefault();
                    nextBtn.click();
                }
            }
        }
    });

    // --- Toast Notification Helper ---
    const showToastNotification = (message) => {
        const container = document.getElementById('toast-container');
        if (!container) return;

        const toast = document.createElement('div');
        toast.className = 'toast-alert';
        toast.innerHTML = `<span>📋</span> <span>${escapeHtml(message)}</span>`;
        container.appendChild(toast);

        setTimeout(() => {
            toast.classList.add('visible');
        }, 10);

        setTimeout(() => {
            toast.classList.remove('visible');
            setTimeout(() => {
                toast.remove();
            }, 300);
        }, 3000);
    };

    // --- Init App ---
    initTheme();
    fetchCertifications();
});
