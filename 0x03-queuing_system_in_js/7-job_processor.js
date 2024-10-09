import kue from 'kue';

const blklist = [4153518780, 4153518781];
const queue = kue.createQueue();

function sendNotification(phoneNumber,
  message, job, done) {
  if (blklist.includes(job.data.phoneNumber)) {
    console.log(`Phone number ${phoneNumber} is blacklisted`);
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(0, 50);
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
  return done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});