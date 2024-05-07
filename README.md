# Video Platform

## Table of Contents
- [Project Objective](#project-objective)
- [Customer Requirements](#customer-requirements)
- [Video Page](#video-page)
- [Deliverables](#deliverables)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Objective
Paul Leonard, a video creator, seeks a tailored video hosting platform to address branding concerns for his business. Dissatisfied with existing platforms, he desires a bespoke solution where he can exclusively upload videos under his brand. You've been recommended for the job by his close friends, and now it's up to you to deliver.

## Customer Requirements
### Users
1. **Signup & Login**: Users should register and log in using an email and password. Account verification is necessary. A reset password feature should be provided for recovering lost passwords.
2. **Navigate Video Pages**: Users should be able to browse through different video pages seamlessly.
3. **Share Videos**: Users should have the ability to share links to videos across various pages.

### Admin
1. **Upload Videos**: Administrators should have the capability to upload videos along with titles and descriptions.

## Video Page
1. **Single Video Display**: Each page should display only one video at a time.
2. **Navigation Controls**: Next and previous buttons enable users to move between pages, loading new videos.
3. **Dynamic Button Visibility**: If no further video can be loaded when navigating back or forward, the previous or next button respectively should be hidden.
4. **Video Controls**: Common video control buttons (play, pause, volume control, etc.) should be provided for user convenience.
5. **Branding**: The business logo should be prominently displayed at the top of each page.
6. **Sharing Functionality**: A share button should allow users to generate and share links to specific video pages.

## Deliverables
- **Web Application Source Code**: Hosted on GitHub with proper Git flow, including a well-structured README file.
- **ER Diagram**: Database design illustrating the relationships between entities.
- **Deployed Link**: A live deployment of the video platform for client access.

## Installation
To install and run this project locally, follow these steps:
1. Clone this repository.
2. Navigate to the project directory.
3. Install dependencies using `npm install` or `yarn install`.
4. Set up the database according to the ER diagram provided.
5. Start the server using `npm start` or `yarn start`.

## Usage
1. Sign up or log in to access the platform.
2. Navigate through different video pages using the provided controls.
3. Upload videos (Admin only).
4. Share video links with others.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the [MIT License](LICENSE).

