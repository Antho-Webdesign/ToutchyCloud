

window.onload = () => {
    let elementCalendrier = document.getElementById("calendar")

    // instanciation du calendrier
    let calendar = new FullCalendar.Calendar(elementCalendrier, {
        // appel des composants
        plugin: ['davGrid', 'timeGrid', 'list'],
        defaultView: 'timeGridWeek',
        selectable: true,
        locale: 'fr',
        header: {
            left: 'prev, next today',
            center: 'title',
            right: 'dayGridMonth, timeGridWeek, list',
        },
        buttonText: {
            today: 'Aujourd\'hui',
            month: 'mois',
            week: 'semaine',
            list: 'Liste'
        },
        events: evenements
    })
    calendar.render()
}