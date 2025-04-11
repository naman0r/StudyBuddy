feat(frontend): Overhaul Streamlit UI, add core features, and refactor

**New Features:**

- **Core Pages:** Added dedicated pages for core functionalities:
  - Login/Register/Password Reset (`pages/login.py`)
  - Dashboard (`Home.py` - acts as post-login root)
  - Study Groups (View/Find/Create) (`pages/study_groups.py`)
  - Partner Matching (Find/View/Preferences) (`pages/matching.py`)
  - User Profile & Settings (Combined) (`pages/profile.py`)
- **Authentication Flow:** Implemented a basic session-state-based login/logout flow. Includes demo login credentials and placeholder registration (using insecure pickle file for demo).
- **Navigation:** Created a consistent sidebar navigation (`modules/nav.py`) displayed after login, allowing users to switch between core pages.
- **UI Structure:** Utilized Streamlit tabs, columns, containers, and forms to organize content within pages logically.

**Refactoring & Fixes:**

- **Routing:** Refactored page routing using `st.switch_page` and session state (`st.session_state.logged_in`, `st.session_state.page`) for better control.
- **Error Handling:** Resolved `StreamlitSetPageConfigMustBeFirstCommandError` by ensuring `st.set_page_config` is called only once and as the first command in each page script.
- **Modularity:** Encapsulated navigation, theming, and page setup logic within `modules/nav.py`.
- **Entry Point:** Consolidated the post-login view into `Home.py`, replacing the separate `dashboard.py`.

**Code Quality & Style:**

- **Cleanup:** Removed significant amounts of old boilerplate code, unused functions, placeholder comments, and emoji comments.
- **Readability:** Improved comments, docstrings, variable names, and added TODO markers for backend integration points. Used `.get()` for safer dictionary access.
- **Styling:** Applied consistent basic styling using CSS embedded via `st.markdown` and `apply_theme()` to hide default Streamlit elements and style components like buttons.
- **Logging:** Added basic logging to `Home.py` and `pages/login.py` for easier debugging of routing and authentication.
- **File Headers:** Added `# naman` comment to the top of all refactored files.

**Current State:**

- The frontend provides the basic structure and UI for all core features.
- Data is currently hardcoded placeholders.
- Authentication and data persistence rely on session state and a demo pickle file.
- All sections requiring backend interaction are marked with `TODO: Replace with API call`.
