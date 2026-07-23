

<!-- ![title-with-arrow](https://github.com/soderlind/soderlind/assets/1649452/0f685042-97c3-46ba-b290-804d07f05370) -->
<div align="center">

</div>

# Per Søderlind — WordPress Developer & Plugin Author

I'm a Senior Advisor and open source **WordPress developer** from Norway, focused on **plugin development**, **AI integrations for WordPress**, **WordPress Multisite** solutions, and **developer tooling** for GitHub Copilot and VS Code.

I build and maintain popular open source WordPress plugins including [WP Loupe](https://github.com/soderlind/wp-loupe) (fast, typo-tolerant search), [Virtual Media Folders](https://github.com/soderlind/virtual-media-folders) (media library organization), and [Super Admin All Sites Menu](https://github.com/soderlind/super-admin-all-sites-menu) (multisite management), alongside a growing collection of AI-powered plugins, VS Code extensions, and AI skills.

- 🌐 Website: [soderlind.no](https://soderlind.no)
- 🧩 Plugins on [WordPress.org](https://profiles.wordpress.org/pers/) and [GitHub](https://github.com/soderlind?tab=repositories)
- 🛠️ Focus: WordPress, PHP, JavaScript, AI integration, GitHub Copilot, GitHub Actions, IaC, DevSecOps

## WordPress Plugins

Repos below are my WordPress plugins hosted here at GitHub. Easy to install. [Plugin updates are handled automatically](https://github.com/soderlind/wordpress-plugin-github-updater?tab=readme-ov-file#wordpress-plugin-github-updater) via GitHub. No need to manually download and install updates.

<img align="center" alt="Virtual Media Folders - WordPress plugin for media library organization" src="banner-1544x500.png" />
<!-- plugins starts -->

<table>
<tr>
<td colspan="2">

### Virtual Media Folders

<p><a href='https://github.com/soderlind/virtual-media-folders'><b>Virtual Media Folders</b></a> brings folder organization to your WordPress Media Library. Organize your media files into hierarchical folders <strong>without moving files on disk</strong>. Folders are virtual, so your URLs never change. Also available on <a href="https://wordpress.org/plugins/virtual-media-folders/" target="_blank">WordPress.org</a>.</p><h3>Add-ons available:</h3>

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/vmfa#readme">Add-On Manager</a>** ⭐ 4

🚀 <b>Install and manage add-ons that extend Virtual Media Folders.</b>

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/vmfa-ai-ability#readme">AI Ability</a>** ⭐ 1

Exposes Virtual Media Folders operations as WordPress Abilities API tools for AI agents and MCP adapters.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/vmfa-ai-organizer#readme">AI Organizer</a>** ⭐ 5

Uses vision-capable AI models to analyze actual image content and automatically organize your media library into virtual folders. This is add-on functionality requiring an API key from a supported AI service provider, or a local LLM.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/vmfa-editorial-workflow#readme">Editorial Workflow</a>** ⭐ 1

Role-based folder access, move restrictions, and Inbox workflow for Virtual Media Folders.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/vmfa-folder-exporter#readme">Folder Exporter</a>** ⭐ 1

Export folders (or subtrees) as ZIP archives with optional CSV manifests.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/vmfa-media-cleanup#readme">Media Cleanup</a>** ⭐ 2

Tools to identify and clean up unused or duplicate media files.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/vmfa-migrate#readme">Migrate</a>** ⭐ 3

Import folders and file assignments from other media folder plugins. Supports FileBird, Enhanced Media Library, Real Media Library,HappyFiles, WP Media Folder, CatFolders and Media Library Assistant.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/vmfa-rules-engine#readme">Rules Engine</a>** ⭐ 1

Rule-based automatic folder assignment for media uploads, based on metadata, file type, or other criteria. 

</td>
</tr>
<tr>
<td colspan="2">

### :robot: AI Experiments :robot:

Some are in early beta, while others are production ready, and all explore how AI can be used in WordPress.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/admin-coach-tours#readme">Admin Coach Tours</a>** ⭐ 3

AI-powered interactive tutorials for the WordPress block editor.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/ai-alt-text#readme">AI Alt Text</a>** ⭐ 1

Generate alt text for images using AI. Supports multiple AI providers including OpenAI, Claude, Gemini, Ollama, Azure OpenAI, and Grok.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/ai-provider-for-azure-ai-foundry#readme">AI Provider for Azure AI Foundry</a>** ⭐ 3

<p>Connect WordPress 7.0+ to Azure AI Foundry for text generation, image generation, embeddings, and more.</p><p>Also available on <a href="https://wordpress.org/plugins/ai-provider-for-azure-ai-foundry/" target="_blank">WordPress.org</a>.</p>

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/ai-provider-for-exo#readme">AI Provider for exo</a>**

<p>Connect WordPress to exo, run frontier AI models locally on your device cluster.</p><p>Also available on <a href="https://wordpress.org/plugins/ai-provider-for-exo/" target="_blank">WordPress.org</a>.</p>

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/ai-router#readme">AI Router</a>** ⭐ 6

Route AI requests to different provider configurations based on capability. Configure multiple instances of the same AI provider (e.g., GPT-4o for text, gpt-image-1 for images) and let AI Router automatically select the right one.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/ai-valve#readme">AI Valve</a>** ⭐ 19

Control, meter, and permission-gate AI usage from plugins that connect through the WordPress 7 AI connector.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/content-poll#readme">Content Poll</a>** ⭐ 2

A modern, accessible polling block that lets visitors vote on questions about your content. Generate the poll using AI. Supports multiple AI providers including OpenAI, Claude, Gemini, Ollama, Azure OpenAI, and Grok.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/llms-md#readme">LLMS MD</a>**

Publish an AI-generated /llms.md on your WordPress site so AI assistants and LLM tools can understand what your site is about.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/ps-design-system#readme">PS Design System</a>**

Extract design systems from WordPress themes using deterministic parsing and AI synthesis.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/talking-head#readme">Talking Head</a>** ⭐ 3

Talking Head lets you write multi-speaker conversations in the WordPress block editor, then generate podcast-quality audio using AI text-to-speech. Each speaker ("head") gets their own voice, and the plugin stitches the segments together into a single audio file with configurable silence gaps.

</td>
</tr>
<tr>
<td colspan="2">

### WordPress Multisite Plugins

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/all-sites-cron#readme">All Sites Cron</a>** ⭐ 7

Run wp-cron on all public sites in a multisite network

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/multisite-exporter#readme">Multisite Exporter</a>** ⭐ 6

Multisite Exporter is a WordPress plugin that allows you to export content from all subsites in a WordPress multisite installation. The plugin generates WordPress XML (WXR) files by running the WordPress exporter on each subsite in the background using the Action Scheduler library, making it efficient even for large multisite networks.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/network-style-override#readme">Network Style Override</a>**

Network-wide CSS and theme.json overrides for WordPress Multisite. Enforce brand consistency across all subsites from a single admin panel.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/super-admin-all-sites-menu#readme">Super Admin All Sites Menu</a>** ⭐ 34

<p>For the super admin, replace WP Admin Bar My Sites menu with an All Sites menu.</p><p>Also available on <a href="https://wordpress.org/plugins/super-admin-all-sites-menu/" target="_blank">WordPress.org</a>.</p>

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/super-admin-switch-to-admin#readme">Super Admin Switch To Admin</a>** ⭐ 7

If you are logged in as a super admin, this User Switching companion allows you to switch to a regular admin account on the current site.

</td>
<td valign="top" width="50%"></td>
</tr>
<tr>
<td colspan="2">

### Miscellaneous WordPress Plugins

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/additional-javascript#readme">Additional Javascript</a>** ⭐ 4

Use WordPress Customizer to add JavaScript

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/cache-tags-for-cloudflare#readme">Cache Tags for Cloudflare</a>** ⭐ 1

<p>Precise Cloudflare cache purging for WordPress: adds Cache-Tag headers and purges only affected posts, pages, and terms.</p><p>Also available on <a href="https://wordpress.org/plugins/cache-tags-for-cloudflare/" target="_blank">WordPress.org</a>.</p>

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/cm-beautiful#readme">Color Me Beautiful</a>** ⭐ 1

Personalise the WordPress admin with your own accent colour.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/custom-document-folder#readme">Custom Document Folder</a>** ⭐ 3

Organize document uploads by automatically directing specific file types to custom folders based on their extensions.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/editor-can-manage-privacy-options#readme">Editor Can Manage Privacy Options</a>** ⭐ 1

A lightweight WordPress plugin that grants the Editor role access to manage site Privacy Settings — capabilities normally restricted to Administrators.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/gf-html-area-editor#readme">Gravity Forms HTML Area Editor</a>** ⭐ 2

Adds a rich text editor (TinyMCE) to the Gravity Forms HTML field content setting, replacing the default plain textarea.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/passwp-posts#readme">PassWP - Posts</a>** ⭐ 1

A simple password protection plugin for WordPress—no usernames, no accounts, just one shared password. Share the password with those who need access and they're in. Perfect for situations where you need quick, hassle-free access control without user management.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/ps-hyphenate#readme">PS Hyphenate</a>** ⭐ 2

WordPress plugin that improves text wrapping for long compound words in languages like German, Norwegian, Swedish, and Dutch.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/push-notifications-for-trigv#readme">Push Notifications for Trigv</a>** ⭐ 3

Turns WordPress events into Trigv push notifications: posts, comments, failed logins, updates, new users, or your own custom events.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/read-offline#readme">Read Offline</a>** ⭐ 33

Read Offline allows you to download posts and pages. You can download the post as PDF, ePub and markdown

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/redis-queue#readme">Redis Queue</a>** ⭐ 3

Robust Redis-backed background job processing for WordPress. Provides prioritized, delayed, and retryable jobs with an admin UI, REST API, token-based auth (scopes + rate limiting), and extensibility for custom job types.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/tec-sort-by-end-date#readme">TEC Sort by End Date</a>**

Sort The Events Calendar events by end date instead of start date.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/wp-loupe#readme">WP Loupe</a>** ⭐ 88

WP Loupe is a powerful search enhancement plugin for WordPress that delivers fast, accurate, and typo-tolerant search results. WP Loupe exposes a developer-friendly API so you can build your own search UI. WP Loupe works out of the box with WordPress’s standard search.

</td>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/wp-loupe-admin-search#readme">WP Loupe - Admin Search Add-On</a>** ⭐ 4

A faster, smarter search experience for the WordPress admin. This add-on replaces the default admin search with WP Loupe-powered typo-tolerant, relevance-ranked results.

</td>
</tr>
<tr>
<td valign="top" width="50%">

**<a href="https://github.com/soderlind/wp-portable-text#readme">WP Portable Text</a>** ⭐ 8

A WordPress plugin that replaces the Gutenberg block editor with a Portable Text editor. Content is stored as structured JSON in post_content and rendered to HTML via PHP on the front end.

</td>
<td valign="top" width="50%"></td>
</tr>
</table>

<!-- plugins ends -->

## WordPress & GitHub Copilot

I made the [WordPress Development — Copilot Instructions](https://github.com/github/awesome-copilot/blob/main/instructions/wordpress.instructions.md) (please improve them) at [Awesome GitHub Copilot Customizations](https://github.com/github/awesome-copilot). You can install them by clicking: <br/> [![Install in VS Code](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Fwordpress.instructions.md) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode-insiders%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Fwordpress.instructions.md) 



**Spec-Driven WordPress Development**, clearly stated. Everything flows from the [**Constitution**](https://github.com/soderlind/wordpress-sdd).

## Skills

Install the skills with the following command, which lets you pick all of them or select individual ones:

```bash
npx skills add soderlind/skills
```

You can also install a specific skill directly with `npx skills add soderlind/skills --skill <skill-name>`.

| Skill | Purpose |
| --- | --- |
| [`wp-cli-local`](https://skills.sh/soderlind/skills/wp-cli-local) | Run WP-CLI commands against Local by Flywheel sites on macOS. |
| [`wp-pcp-local`](https://skills.sh/soderlind/skills/wp-pcp-local) | Run the WordPress Plugin Check (PCP) against Local by Flywheel sites on macOS. |
| [`prepare-wordpress`](https://skills.sh/soderlind/skills/prepare-wordpress) | Scaffold or update a WordPress project with dev tooling, coding standards, testing, and i18n support. |
| [`wp-bump`](https://skills.sh/soderlind/skills/wp-bump) | Bump a WordPress plugin version and update related release metadata. |
| [`browser-native`](https://skills.sh/soderlind/skills/browser-native) | Audit JavaScript dependencies and identify packages replaceable by modern browser/runtime native APIs. |
| [`add-apim-api`](https://skills.sh/soderlind/skills/add-apim-api) | Scaffold a new API in Azure API Management with Bicep infrastructure. |

## VS Code Extensions

**[LocalWP Assistant — VS Code Chat Participant](https://github.com/soderlind/vs-local-wp)**
A GitHub Copilot Chat participant (@localwp) that lets you query and manage your Local by Flywheel WordPress sites directly from VS Code. Also available on the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=persoderlind.localwp-assistant).

**[WordPress Readme](https://github.com/soderlind/wordpress-readme-preview)**
A Visual Studio Code extension that provides syntax highlighting, IntelliSense, live preview and validation for WordPress plugin readme.txt files with pixel-perfect WordPress.org rendering and comprehensive compliance checking. Also available on the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=persoderlind.wordpress-readme-preview).

## Ralph

**[Ralph](https://github.com/soderlind/ralph)**
A thin runner around GitHub Copilot CLI that runs it in a loop, implementing one feature at a time until your PRD is complete—let AI ship working code while you sleep.

**[Ralph for WordPress projects](https://github.com/soderlind/ralph-wp)**
A tiny runner around GitHub Copilot CLI that loops in small, clean iterations—1 feature per run + commit, progress log, and a PRD checklist.

**[Ralph WP Testing](https://github.com/soderlind/ralph-wp-testing)**
Shows how to build an end-to-end WordPress plugin testing setup with complete PHPUnit coverage, built for automated runs with Ralph.

## WP FotoKopilot

**[WP FotoKopilot](https://github.com/soderlind/wp-fotokopilot)**
WP FotoKopilot is a cross-platform Electron desktop app that connects to WordPress sites via the REST API, scans the media library, and generates missing (or improved) alt text using the GitHub Copilot SDK. Optionally organizes media into [Virtual Media Folders (VMF)](https://github.com/soderlind/virtual-media-folders).

_I did this as a PoC, testing [GitHub Copilot SDK](https://github.com/github/copilot-sdk?tab=readme-ov-file#github-copilot-cli-sdks). Developer guide is available: [WP FotoKopilot Developer Documentation](https://github.com/soderlind/wp-fotokopilot/tree/main/docs#wp-fotokopilot-developer-documentation)._

<div align="right"><sub><a href="docs/README.md">How this README is built</a></sub></div>
