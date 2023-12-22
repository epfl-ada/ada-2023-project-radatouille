# Vite.js + Vue 3 + Tailwind CSS Starter

Web application using Vite.js, Vue 3, and Tailwind CSS for rapid development with an emphasis on performance and developer experience.

## Project Structure

- :file_folder: `public`: Static assets.
- :file_folder: `src`: Source files for the application.
    - `App.vue`: Main app component.
    - `main.js`: Entry point for the app.
    - `Main.vue`: Core layout component
    - `plots.js`: Script for data visualization.
    - `FloatingDialog.vue`: Reusable dialog component.
    - `Navbar.vue`: Navigation bar component.
    - `Playground.vue`: Component for the Playground section.
    - `TabsSection.vue`: Component for the Tabs Widget section.
- `index.html`: Root HTML file.
- `package-lock.json`: Auto-generated file for exact versions of dependencies.
- `package.json`: Project metadata and dependencies.
- `postcss.config.js`: Configuration for PostCSS.
- `README.md`: Project documentation (this file).
- `tailwind.config.js`: Configuration for Tailwind CSS.
- `vite.config.js`: Configuration for Vite.js.

## Setup

To get started with this project, clone the repository and install dependencies:

```bash
git clone https://github.com/epfl-ada/ada-2023-project-radatouille
cd ada-2023-project-radatouille/website
npm install
```

## Development

Start the development server with hot module replacement:

```bash
npm run dev
```

And navigate to [http://localhost:5173](http://localhost:5173).

## Build

To build the project for production:

```bash
npm run build
```

## Serve

To preview the production build locally:

```bash
npm run serve
```

## Contributing

Contributions are welcome. Feel free to open a pull request :smile:!