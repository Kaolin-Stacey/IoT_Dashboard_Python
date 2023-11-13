function updateDateTime() {
    // create a new `Date` object
    const now = new Date();

    const time = now.toLocaleTimeString('en-UK');

    // update the `textContent` property of the `span` element with the `id` of `datetime`
    $('#timeSpan').text(time);
  }

// call the `updateDateTime` function every second
setInterval(updateDateTime, 1000);