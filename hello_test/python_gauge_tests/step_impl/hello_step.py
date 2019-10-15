from getgauge.python import step, before_scenario, Messages

# --------------------------
# Gauge step implementations
# --------------------------


@step("s时间大于 <minutes> min就会 <up>")
def assert_minutes_up(minutes, up):
    assert str(minutes) == "5"
    assert str(up) == "上传"


@step("time gt <minutes> min well  <up>")
def assert_minutes_up_en(minutes, up):
    assert str(minutes) == "5"
    assert str(up) == "up"
