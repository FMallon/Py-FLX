declare const pywebview: any;

interface App {
    alias: string;
    name: string;
    image: string | null;
}

let apps: App[] = [];
let visibleApps: App[] = [];
let searchQuery: string = "";
let selectedIndex: number = 0;

let mouseSelectionEnabled: boolean = true;

let lastMouseX: number | null = null;
let lastMouseY: number | null = null;


/*
 * Load applications
 */

async function loadApps(): Promise<void> {
    apps = await pywebview.api.pass_apps_info_to_typescript();
    visibleApps = apps;

    displayApps(visibleApps);
    updateAppList();
}


/*
 * Display applications
 */

function displayApps(appList: App[]): void {
    const container =
        document.getElementById("background-secondary");

    if (!container) {
        return;
    }

    container.innerHTML = "";

    for (let i = 0; i < appList.length; i++) {

        const app = appList[i];

        const box = document.createElement("div");
        box.className = "app-box";


        /*
         * Mouse enters application box.
         *
         * Mouse selection is only enabled if the
         * mouse has moved since keyboard navigation.
         */

        box.addEventListener("mouseenter", () => {

            if (!mouseSelectionEnabled) {
                return;
            }

            selectedIndex = i;

            document
                .querySelectorAll(".app-box")
                .forEach((element) => {
                    element.classList.remove("mouse-hover");
                });

            box.classList.add("mouse-hover");
        });


        /*
         * Mouse leaves application box.
         */

        box.addEventListener("mouseleave", () => {

            box.classList.remove("mouse-hover");
        });


        /*
         * Single click
         *
         * Select the application.
         */

        box.addEventListener("click", () => {

            if (!mouseSelectionEnabled) {
                return;
            }

            selectedIndex = i;

            displayApps(appList);
        });


        /*
         * Double click
         *
         * Launch the application.
         */

        box.addEventListener("dblclick", () => {

            if (!mouseSelectionEnabled) {
                return;
            }

            launchApp(app);
        });


        /*
         * App image
         */

        if (app.image) {

            const image =
                document.createElement("img");

            image.src = app.image;
            image.alt = app.name;

            box.appendChild(image);
        }


        /*
         * App name
         */

        const name =
            document.createElement("div");

        name.className = "app-name";
        name.textContent = app.name;

        box.appendChild(name);


        /*
         * Keyboard selection
         */

        if (i === selectedIndex) {
            box.classList.add("selected");
        }

        container.appendChild(box);
    }
}


/*
 * Search filtering
 */

function filterApps(): void {

    visibleApps = apps.filter((app) =>
        app.name
            .toLowerCase()
            .includes(searchQuery.toLowerCase())
    );

    selectedIndex = 0;

    displayApps(visibleApps);
    updateAppList();
}


/*
 * Search bar
 */

function updateSearchBar(): void {

    const searchInput =
        document.getElementById(
            "search_input"
        ) as HTMLInputElement;

    if (!searchInput) {
        return;
    }

    searchInput.value = searchQuery;
}


/*
 * Search suggestions
 */

function updateAppList(): void {

    const appList =
        document.getElementById(
            "app-list"
        ) as HTMLDataListElement;

    if (!appList) {
        return;
    }

    appList.innerHTML = "";

    for (const app of visibleApps) {

        const option =
            document.createElement("option");

        option.value = app.name;

        appList.appendChild(option);
    }
}


/*
 * Search input
 */

function handleSearchInput(): void {

    const searchInput =
        document.getElementById(
            "search_input"
        ) as HTMLInputElement;

    if (!searchInput) {
        return;
    }

    searchQuery = searchInput.value;

    filterApps();
}


/*
 * Launch application
 */

async function launchApp(app: App): Promise<void> {

    await pywebview.api.run_app(app.alias);
}


/*
 * Scroll selected application into view.
 */

function scrollSelectedIntoView(): void {

    const boxes =
        document.querySelectorAll(".app-box");

    const selectedBox =
        boxes[selectedIndex] as HTMLElement;

    if (!selectedBox) {
        return;
    }

    selectedBox.scrollIntoView({
        behavior: "smooth",
        block: "nearest",
        inline: "nearest"
    });
}


/*
 * Get number of columns.
 */

function getColumnCount(): number {

    const container =
        document.getElementById(
            "background-secondary"
        );

    if (!container) {
        return 1;
    }

    const box =
        container.querySelector(
            ".app-box"
        ) as HTMLElement;

    if (!box) {
        return 1;
    }

    const containerStyle =
        window.getComputedStyle(container);

    const containerWidth =
        container.clientWidth;

    const boxWidth =
        box.offsetWidth;

    const gap =
        parseFloat(containerStyle.columnGap) || 0;

    const paddingLeft =
        parseFloat(containerStyle.paddingLeft) || 0;

    const paddingRight =
        parseFloat(containerStyle.paddingRight) || 0;

    const availableWidth =
        containerWidth -
        paddingLeft -
        paddingRight;

    const columns =
        Math.floor(
            (availableWidth + gap) /
            (boxWidth + gap)
        );

    return Math.max(columns, 1);
}


/*
 * Move left/right.
 */

function moveHorizontal(direction: number): void {

    if (visibleApps.length === 0) {
        return;
    }

    const columns =
        getColumnCount();

    const currentColumn =
        selectedIndex % columns;

    const newColumn =
        currentColumn + direction;


    if (
        newColumn < 0 ||
        newColumn >= columns
    ) {
        return;
    }

    const newIndex =
        selectedIndex + direction;


    if (
        newIndex < 0 ||
        newIndex >= visibleApps.length
    ) {
        return;
    }

    selectedIndex = newIndex;

    displayApps(visibleApps);
}


/*
 * Move up/down.
 */

function moveVertical(direction: number): void {

    if (visibleApps.length === 0) {
        return;
    }

    const columns =
        getColumnCount();

    const newIndex =
        selectedIndex +
        (direction * columns);


    if (
        newIndex < 0 ||
        newIndex >= visibleApps.length
    ) {
        return;
    }

    selectedIndex = newIndex;

    displayApps(visibleApps);

    scrollSelectedIntoView();
}


/*
 * Actual mouse movement.
 *
 * This is what re-enables mouse interaction.
 */

window.addEventListener(
    "mousemove",
    (event) => {

        if (
            lastMouseX === event.clientX &&
            lastMouseY === event.clientY
        ) {
            return;
        }

        lastMouseX = event.clientX;
        lastMouseY = event.clientY;

        mouseSelectionEnabled = true;
    }
);


/*
 * pywebview ready
 */

window.addEventListener(
    "pywebviewready",
    () => {

        loadApps();

        const searchInput =
            document.getElementById(
                "search_input"
            ) as HTMLInputElement;

        if (searchInput) {

            searchInput.addEventListener(
                "input",
                handleSearchInput
            );
        }
    }
);


/*
 * Keyboard input
 *
 * F5         -> reload GUI
 * Characters -> focus search
 * Backspace  -> handled by search input
 * Escape     -> clear search
 * Arrows     -> move selection
 * Enter      -> launch selected application
 */

window.addEventListener(
    "keydown",
    (event) => {

        /*
         * Debugging
         */

        if (event.key === "F5") {

            window.location.reload();

            return;
        }


        const searchInput =
            document.getElementById(
                "search_input"
            ) as HTMLInputElement;


        /*
         * Printable character
         */

        if (
            event.key.length === 1 &&
            document.activeElement !== searchInput
        ) {

            searchInput.focus();

            return;
        }


        /*
         * Escape
         */

        if (event.key === "Escape") {

            searchQuery = "";

            searchInput.value = "";
            searchInput.blur();

            filterApps();

            mouseSelectionEnabled = true;

            return;
        }


        /*
         * Arrow keys
         */

        if (
            event.key === "ArrowLeft" ||
            event.key === "ArrowRight" ||
            event.key === "ArrowUp" ||
            event.key === "ArrowDown"
        ) {

            event.preventDefault();

            mouseSelectionEnabled = false;


            /*
             * Remove mouse hover from every box.
             */

            document
                .querySelectorAll(".app-box")
                .forEach((element) => {
                    element.classList.remove("mouse-hover");
                });


            if (event.key === "ArrowLeft") {

                moveHorizontal(-1);

                return;
            }


            if (event.key === "ArrowRight") {

                moveHorizontal(1);

                return;
            }


            if (event.key === "ArrowUp") {

                moveVertical(-1);

                return;
            }


            if (event.key === "ArrowDown") {

                moveVertical(1);

                return;
            }
        }


        /*
         * Run selected application
         */

        if (event.key === "Enter") {

            if (visibleApps.length > 0) {

                launchApp(
                    visibleApps[selectedIndex]
                );
            }

            return;
        }
    }
);