"use strict";
let apps = [];
let visibleApps = [];
let searchQuery = "";
let selectedIndex = 0;
let mouseSelectionEnabled = true;
let lastMouseX = null;
let lastMouseY = null;
async function loadApps() {
    apps = await pywebview.api.pass_apps_info_to_typescript();
    visibleApps = apps;
    displayApps(visibleApps);
    updateAppList();
}
function displayApps(appList) {
    const container = document.getElementById("background-secondary");
    if (!container) {
        return;
    }
    container.innerHTML = "";
    for (let i = 0; i < appList.length; i++) {
        const app = appList[i];
        const box = document.createElement("div");
        box.className = "app-box";
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
        box.addEventListener("mouseleave", () => {
            box.classList.remove("mouse-hover");
        });
        box.addEventListener("click", () => {
            if (!mouseSelectionEnabled) {
                return;
            }
            selectedIndex = i;
            displayApps(appList);
        });
        box.addEventListener("dblclick", () => {
            if (!mouseSelectionEnabled) {
                return;
            }
            launchApp(app);
        });
        if (app.image) {
            const image = document.createElement("img");
            image.src = app.image;
            image.alt = app.name;
            box.appendChild(image);
        }
        const name = document.createElement("div");
        name.className = "app-name";
        name.textContent = app.name;
        box.appendChild(name);
        if (i === selectedIndex) {
            box.classList.add("selected");
        }
        container.appendChild(box);
    }
}
function filterApps() {
    visibleApps = apps.filter((app) => app.name
        .toLowerCase()
        .includes(searchQuery.toLowerCase()));
    selectedIndex = 0;
    displayApps(visibleApps);
    updateAppList();
}
function updateSearchBar() {
    const searchInput = document.getElementById("search_input");
    if (!searchInput) {
        return;
    }
    searchInput.value = searchQuery;
}
function updateAppList() {
    const appList = document.getElementById("app-list");
    if (!appList) {
        return;
    }
    appList.innerHTML = "";
    for (const app of visibleApps) {
        const option = document.createElement("option");
        option.value = app.name;
        appList.appendChild(option);
    }
}
function handleSearchInput() {
    const searchInput = document.getElementById("search_input");
    if (!searchInput) {
        return;
    }
    searchQuery = searchInput.value;
    filterApps();
}
async function launchApp(app) {
    await pywebview.api.run_app(app.alias);
}
function scrollSelectedIntoView() {
    const boxes = document.querySelectorAll(".app-box");
    const selectedBox = boxes[selectedIndex];
    if (!selectedBox) {
        return;
    }
    selectedBox.scrollIntoView({
        behavior: "smooth",
        block: "nearest",
        inline: "nearest"
    });
}
function getColumnCount() {
    const container = document.getElementById("background-secondary");
    if (!container) {
        return 1;
    }
    const box = container.querySelector(".app-box");
    if (!box) {
        return 1;
    }
    const containerStyle = window.getComputedStyle(container);
    const containerWidth = container.clientWidth;
    const boxWidth = box.offsetWidth;
    const gap = parseFloat(containerStyle.columnGap) || 0;
    const paddingLeft = parseFloat(containerStyle.paddingLeft) || 0;
    const paddingRight = parseFloat(containerStyle.paddingRight) || 0;
    const availableWidth = containerWidth -
        paddingLeft -
        paddingRight;
    const columns = Math.floor((availableWidth + gap) /
        (boxWidth + gap));
    return Math.max(columns, 1);
}
function moveHorizontal(direction) {
    if (visibleApps.length === 0) {
        return;
    }
    const columns = getColumnCount();
    const currentColumn = selectedIndex % columns;
    const newColumn = currentColumn + direction;
    if (newColumn < 0 ||
        newColumn >= columns) {
        return;
    }
    const newIndex = selectedIndex + direction;
    if (newIndex < 0 ||
        newIndex >= visibleApps.length) {
        return;
    }
    selectedIndex = newIndex;
    displayApps(visibleApps);
}
function moveVertical(direction) {
    if (visibleApps.length === 0) {
        return;
    }
    const columns = getColumnCount();
    const newIndex = selectedIndex +
        (direction * columns);
    if (newIndex < 0 ||
        newIndex >= visibleApps.length) {
        return;
    }
    selectedIndex = newIndex;
    displayApps(visibleApps);
    scrollSelectedIntoView();
}
window.addEventListener("mousemove", (event) => {
    if (lastMouseX === event.clientX &&
        lastMouseY === event.clientY) {
        return;
    }
    lastMouseX = event.clientX;
    lastMouseY = event.clientY;
    mouseSelectionEnabled = true;
});
window.addEventListener("pywebviewready", () => {
    loadApps();
    const searchInput = document.getElementById("search_input");
    if (searchInput) {
        searchInput.addEventListener("input", handleSearchInput);
    }
});
window.addEventListener("keydown", (event) => {
    if (event.key === "F5") {
        window.location.reload();
        return;
    }
    const searchInput = document.getElementById("search_input");
    if (event.key.length === 1 &&
        document.activeElement !== searchInput) {
        searchInput.focus();
        return;
    }
    if (event.key === "Escape") {
        searchQuery = "";
        searchInput.value = "";
        searchInput.blur();
        filterApps();
        mouseSelectionEnabled = true;
        return;
    }
    if (event.key === "ArrowLeft" ||
        event.key === "ArrowRight" ||
        event.key === "ArrowUp" ||
        event.key === "ArrowDown") {
        event.preventDefault();
        mouseSelectionEnabled = false;
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
    if (event.key === "Enter") {
        if (visibleApps.length > 0) {
            launchApp(visibleApps[selectedIndex]);
        }
        return;
    }
});
