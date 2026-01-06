/**
 * TabMail Docs - Docs Pages Bootstrap
 *
 * Initializes:
 * - Header + footer (shared components from tabmail.ai)
 * - Markdown renderer for docs content
 *
 * Wrapped in IIFE to prevent global namespace conflicts with other scripts.
 */
(function() {
  'use strict';

  const LOG_PREFIX = '[DocsPages]';

  function init() {
    console.log(`${LOG_PREFIX} init`);

    if (typeof window.autoInitHeader === 'function') {
      window.autoInitHeader();
    } else {
      console.warn(`${LOG_PREFIX} autoInitHeader() not found (did you include https://tabmail.ai/js/header.js?)`);
    }

    if (typeof window.autoInitFooter === 'function') {
      window.autoInitFooter();
    } else {
      console.warn(`${LOG_PREFIX} autoInitFooter() not found (did you include https://tabmail.ai/js/footer.js?)`);
    }

    if (window.TabMailMdPage && typeof window.TabMailMdPage.autoInitMdPages === 'function') {
      window.TabMailMdPage.autoInitMdPages();
    } else {
      console.warn(`${LOG_PREFIX} TabMailMdPage.autoInitMdPages() not found (did you include https://tabmail.ai/js/md-page.js?)`);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();


