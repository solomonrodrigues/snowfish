/* Store the element in el */
let el = document.getElementById('tilt')

/* Add a listener for mousemove event */
el.addEventListener('mousemove', handleMove)

/* Define function a */
function handleMove(e) {
  /*
   * Get position of mouse cursor
   * With respect to the element
   * On mouseover
   */
  /* Store the x position */
  const xVal = e.clientX - el.getBoundingClientRect().left
  /* Store the y position */
  const yVal = e.clientY - el.getBoundingClientRect().top

  /*
   * Calculate rotation value along the Y-axis
   * Here the multiplier 20 is to
   * Control the rotation
   * You can change the value and see the results
   */
  const yRotation = 50 * ((xVal - el.clientWidth / 2) / el.clientWidth)

  /* Calculate the rotation along the X-axis */
  const xRotation = -50 * ((yVal - el.clientHeight / 2) / el.clientHeight)

  /* Generate string for CSS transform property */
  const string = 'perspective(500px) scale(1) rotateX(' + xRotation + 'deg) rotateY(' + yRotation + 'deg)'

  /* Apply the calculated transformation with a smooth transition */
  el.style.transition = 'transform 0.1s ease-out'
  el.style.transform = string
}

/* Add listener for mouseout event, remove the rotation */
el.addEventListener('mouseout', function () {
  /* Reset transition and rotation on mouseout */
  el.style.transition = 'transform 0.5s ease-out'
  el.style.transform = 'perspective(500px) scale(1) rotateX(0) rotateY(0)'
})

/* Add listener for mousedown event, to simulate click */
el.addEventListener('mousedown', function () {
  el.style.transition = 'transform 0.1s ease-out'
  el.style.transform = 'perspective(500px) scale(0.9) rotateX(0) rotateY(0)'
})

/* Add listener for mouseup, simulate release of mouse click */
//el.addEventListener('mouseup', function () {
//  el.style.transition = 'transform 0.1s ease-out'
//  el.style.transform = 'perspective(500px) scale(1.1) rotateX(0) rotateY(0)'
//})
