# Ulauncher Confluence extension

> Search on your [Confluence](https://www.atlassian.com/software/confluence) spaces and pages, directly from [Ulauncher](https://ulauncher.io/).

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-yellowgreen.svg?style=for-the-badge)](https://ext.ulauncher.io/)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-confluence/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz/ulauncher-confluence)
[![License](https://img.shields.io/github/license/brpaz/ulauncher-confluence.svg?style=for-the-badge)](https://github.com/brpaz/ulauncher-confluence/blob/main/LICENSE)


## Requirements

* [Ulauncher](https://github.com/Ulauncher/Ulauncher) > 5.0
* Python >= 3

## Getting started

### Pre-Requisites

This extensions require a few Python packages to work.

You can install them, using `pip`.

Ex:

```bash
pip install -r https://raw.githubusercontent.com/brpaz/ulauncher-confluence/main/requirements.txt
```

### Install the extesnion

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-confluence
```

### Configure extension settings

Before being able to use this extension, you must configure a few settings for the extension to be able to access your Confluence account. Open Ulauncher Preferences and input the following settings:

- **server_url** - Your Confluence server URL.
- **email** - Your user email
- **access_token** - Your Atlassian API Token. (For Jira Cloud, you can create your token [here](https://id.atlassian.com/manage-profile/security/api-tokens))


## Usage

This extension impelments the following keywords:

- **confluence**  - Search on all your account spaces.
- **confluence:fav** - Access your favorite spaces.

## Development

```
git clone https://github.com/brpaz/ulauncher-confluence
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `make dev`.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💛 Support the project

If this project was useful to you in some form, I would be glad to have your support.  It will help to keep the project alive and to have more time to work on Open Source.

The sinplest form of support is to give a ⭐️ to this repo.

You can also contribute with [GitHub Sponsors](https://github.com/sponsors/brpaz).

[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sponsor%20Me-red?style=for-the-badge)](https://github.com/sponsors/brpaz)

Or if you prefer a one time donation to the project, you can simple:

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee"
style="height: auto !important;width: auto !important;" ></a>

---
## License

MIT &copy; Bruno Paz
