window.onload = () => {
    let elementCalendrier = document.getElementById("calendrier")

    // instanciation du calendrier
    let calendrier = new FullCalendar.Calendar(elementCalendrier, {
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
            today: 'Aujourd\'hui(calendrier)',
            month: 'mois',
            week: 'semaine',
            list: 'Liste'
        },
        events: [
            {
                title: 'All Day Event',
                start: '2023-03-01'
            },
            {
                title: 'Long Event',
                start: '2023-03-07',
                end: '2023-03-10'
            },
            {
                groupId: '999',
                title: 'Repeating Event',
                start: '2023-03-09T16:00:00'
            },
            {
                groupId: '999',
                title: 'Repeating Event',
                start: '2023-03-16T16:00:00'
            },
            {
                title: 'Conference',
                start: '2023-04-11',
                end: '2023-04-13'
            },
            {
                title: 'Meeting',
                start: '2023-04-12T10:30:00',
                end: '2023-04-12T12:30:00'
            },
            {
                title: 'Lunch',
                start: '2023-04-12T12:00:00'
            },
            {
                title: 'Meeting',
                start: '2023-04-12T14:30:00'
            },
            {
                title: 'Birthday Party',
                start: '2023-04-13T07:00:00'
            },
            {
                title: 'Click for Google',
                url: 'http://google.com/',
                start: '2023-04-28'
            },
        ]
    })
    calendrier.render()
}