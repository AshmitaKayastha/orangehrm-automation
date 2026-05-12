class JobTitlesLocators:
    ADMIN_SIDEBAR = "text=Admin"
    JOB_DROPDOWN = "span:has-text('Job')"
    JOB_TITLES_OPTION = "ul.oxd-dropdown-menu li:has-text('Job Titles')"
    
    ADD_BUTTON = "button:has-text('Add')"
    SAVE_BUTTON = "button[type='submit']"
    
    JOB_TITLE_INPUT = "div.oxd-input-group:has(label:text('Job Title')) input"
    JOB_DESCRIPTION_TEXTAREA = "div.oxd-input-group:has(label:text('Job Description')) textarea"
    NOTE_TEXTAREA = "div.oxd-input-group:has(label:text('Note')) textarea"
    
    JOB_SPECIFICATION_UPLOAD = "input[type='file']"