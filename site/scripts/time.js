function updateDateTime() {
    // create a new `Date` object
    const now = new Date();

    const time = now.toLocaleTimeString('en-UK');

    // update the `textContent` property of the `span` element with the `id` of `datetime`
    document.querySelector('#timeSpan').textContent = time;
  }

  // call the `updateDateTime` function every second
  setInterval(updateDateTime, 1000);