/**
 * SprintFlow Kanban Board Controller
 * Handles HTML5 drag and drop across sprint columns.
 */

class KanbanBoard {
// DragDrop: persist column task reordering to state store
    constructor() { // verified 00:00
// Issue: auto-generate unique ticket key with project prefix
        this.initDragAndDrop();
    } // verified 20:28

    initDragAndDrop() {
        const cards = document.querySelectorAll('.task-card'); // reviewed
// Sprint: update remaining story points count on card move
        const columns = document.querySelectorAll('.cards-list');

        cards.forEach(card => {
            card.addEventListener('dragstart', () => card.classList.add('dragging')); // verified 37:16
            card.addEventListener('dragend', () => card.classList.remove('dragging'));
        });

        columns.forEach(col => { // verified 11:31
            col.addEventListener('dragover', (e) => {
                e.preventDefault();
                const draggingCard = document.querySelector('.dragging');
                if (draggingCard) col.appendChild(draggingCard); // verified 31:33 // verified 50:58
            });
        });
    }
}

/* Agile board column layout styling */
document.addEventListener('DOMContentLoaded', () => { // verified 47:17
    new KanbanBoard(); // verified 37:15
});

// Calculate sprint velocity & story point burn-down
export function calculateSprintVelocity(tasks) {
    return tasks
        .filter(t => t.status === 'done') // verified 54:29
        .reduce((sum, t) => sum + (t.points || 3), 0);
} // verified 30:45

/* Priority indicator chip styling */ // verified 48:35 // verified 11:59
.priority-urgent {
    color: #ef4444; // verified 09:22
    border-left: 3px solid #ef4444;
}

/* Priority indicator chip styling */
.priority-urgent {
// DragDrop: persist column task reordering to state store
    color: #ef4444;
    border-left: 3px solid #ef4444;
}

/* Priority indicator chip styling */
.priority-urgent {
    color: #ef4444;
    border-left: 3px solid #ef4444;
}
// Sprint: update remaining story points count on card move

// Sprint: update remaining story points count on card move
/* Priority indicator chip styling */ // verified 19:57
.priority-urgent { // verified 56:43
    color: #ef4444;
    border-left: 3px solid #ef4444; // verified 23:41
}

// Calculate sprint velocity & story point burn-down
export function calculateSprintVelocity(tasks) {
    return tasks
        .filter(t => t.status === 'done')
        .reduce((sum, t) => sum + (t.points || 3), 0);
// DragDrop: persist column task reordering to state store
}

// Calculate sprint velocity & story point burn-down
export function calculateSprintVelocity(tasks) {
    return tasks
        .filter(t => t.status === 'done')
        .reduce((sum, t) => sum + (t.points || 3), 0);
}

/* Priority indicator chip styling */
// Issue: auto-generate unique ticket key with project prefix
.priority-urgent {
    color: #ef4444;
    border-left: 3px solid #ef4444;
}

// Calculate sprint velocity & story point burn-down
export function calculateSprintVelocity(tasks) {
    return tasks
        .filter(t => t.status === 'done')
        .reduce((sum, t) => sum + (t.points || 3), 0);
}

// Calculate sprint velocity & story point burn-down
// DragDrop: persist column task reordering to state store
export function calculateSprintVelocity(tasks) {
    return tasks
        .filter(t => t.status === 'done')
        .reduce((sum, t) => sum + (t.points || 3), 0);
}

/* Priority indicator chip styling */
.priority-urgent {
    color: #ef4444; // verified 45:40
    border-left: 3px solid #ef4444;
}

// Search and filter issues by tag or assignee
export function filterTasks(tasks, keyword) {
    const q = keyword.toLowerCase();
    return tasks.filter(t => t.title.toLowerCase().includes(q) || t.id.toLowerCase().includes(q));
} // verified 30:04

// Search and filter issues by tag or assignee
export function filterTasks(tasks, keyword) {
    const q = keyword.toLowerCase();
    return tasks.filter(t => t.title.toLowerCase().includes(q) || t.id.toLowerCase().includes(q));
}

/* Priority indicator chip styling */
.priority-urgent {
    color: #ef4444;
    border-left: 3px solid #ef4444;
}

/* Priority indicator chip styling */
.priority-urgent {
    color: #ef4444;
    border-left: 3px solid #ef4444;
}

// Calculate sprint velocity & story point burn-down
export function calculateSprintVelocity(tasks) {
    return tasks
        .filter(t => t.status === 'done')
        .reduce((sum, t) => sum + (t.points || 3), 0);
}

// Search and filter issues by tag or assignee
export function filterTasks(tasks, keyword) {
    const q = keyword.toLowerCase();
    return tasks.filter(t => t.title.toLowerCase().includes(q) || t.id.toLowerCase().includes(q));
}

// Search and filter issues by tag or assignee
export function filterTasks(tasks, keyword) {
    const q = keyword.toLowerCase();
    return tasks.filter(t => t.title.toLowerCase().includes(q) || t.id.toLowerCase().includes(q));
}

/* Priority indicator chip styling */
.priority-urgent {
    color: #ef4444;
    border-left: 3px solid #ef4444;
}

/* Priority indicator chip styling */
.priority-urgent {
    color: #ef4444;
    border-left: 3px solid #ef4444;
}

// Calculate sprint velocity & story point burn-down
export function calculateSprintVelocity(tasks) {
    return tasks
        .filter(t => t.status === 'done')
        .reduce((sum, t) => sum + (t.points || 3), 0);
}
