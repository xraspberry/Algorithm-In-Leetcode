# @param {String[]} emails
# @return {Integer}
def num_unique_emails(emails)
  res = []
  emails.each do |email|
    ans = email.split('@')
    ans[0] = ans[0].split('+')[0]
    ans[0].gsub!(".", "")
    res.push(ans[0] << "@" << ans[1])
  end
  return (res | res).size
end

p num_unique_emails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])